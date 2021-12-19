from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse

from .models import Category, Blog
from .forms import CommentCreateForm


def index(request):
    return redirect('blog:blog_list')
    # return render(request, 'blog/index.html')

def contact(request):
    return render(request, 'blog/contact.html')

def about(request):
    return render(request, 'blog/about.html')


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('blog:login')
    success_message = 'You have successfully created a new account and you can log in now'


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'blog/login.html'
    success_message = "You have successfully logged in now"


class BlogList(ListView):
    model = Blog
    paginate_by = 10


class AuthorBlogList(BlogList):
    def get_queryset(self):
        # self.kwargs is a dictionary containing in url <>
        # e.g if the url pattern = 'author/<int:username>/<int:year>/', 
        # then the self.kwargs will be {'username': 'user10', 'year': 1}
        self.author = get_object_or_404(User, username=self.kwargs.get('username'))
        author_blog_list = Blog.objects.filter(author=self.author)
        return author_blog_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.author
        return context

class CategoryBlogList(BlogList):
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        category_blog_list = Blog.objects.filter(category=self.category)
        return category_blog_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


# class BlogDetail(DetailView):
#     model = Blog
#
#     def post(self, request, *args, **kwargs):
#         blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
#         comment_form = CommentCreateForm(self.request.POST)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.blog = blog
#             comment.author = self.request.user
#             comment.save()
#             return

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.author = request.user
            comment.save()
            return redirect('blog:blog_detail', pk=pk)
    else:
        form = CommentCreateForm()
    context = {
        'object': blog,
        'form': form
    }
    return render(request, 'blog/blog_detail.html', context)


# Blog CRUD
class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Blog
    fields = ['category', 'title', 'description', 'content', 'title_image']
    success_message = 'You have successfully created a new article'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed (e.g. setting the author to request.user)
        # We should not put 'author' in the fields if we need this 'setting the author' to work
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

    # Change the default dashes in Django Createview form
    def get_form(self):
        form = super(CreateView, self).get_form()
        form.fields['category'].empty_label = "Select a Category"
        return form


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Blog
    fields = ['category', 'title', 'description', 'content', 'title_image']
    success_message = 'You have successfully edited an article'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

    def test_func(self):
        # make sure that only the author can edit his blog
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')

    def test_func(self):
        # make sure that only the author can delete his blog
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False

    # SuccessMessageMixin does not exist in DeleteView and I have to rewrite messages myself
    def get_success_url(self):
        messages.success(self.request, "You have successfully deleted an article")
        return reverse('blog:blog_list')


def contact(request):
    return render(request, 'blog/contact.html')


# like or unlike ajax call
def like_unlike(request):
    if request.POST.get('action') == 'post':
        article_id = int(request.POST.get('article_id'))
        blog = get_object_or_404(Blog, id=article_id)
        if request.user.is_authenticated:
            if request.user in blog.likes.all():
                blog.likes.remove(request.user)
            else:
                blog.likes.add(request.user)
            likes_count = blog.likes.count()
            response = {'likes_count': likes_count}
        else:
            pass
        return JsonResponse(response)


# validate register form before submit
def register_check(request):
    username = request.GET.get('username', None)
    password1 = request.GET.get('password1', None)
    password2 = request.GET.get('password2', None)
    error = {}
    if User.objects.filter(username=username).exists():
        error = {'username_is_taken': True}
    elif not username:
        error = {'username_is_empty': True}
    elif not password1:
        error = {'password1_is_empty': True}
    elif not password2:
        error = {'password2_is_empty': True}
    elif len(password1) < 8:
        error = {'password_lt8': True}
    elif password1.isdecimal():
        error = {'password_only_numeric': True}
    elif password1 != password2:
        error = {'passwords_not_same': True}
    return JsonResponse(error)


# validate login form before submit
def login_check(request):
    username = request.GET.get('username', None)
    password = request.GET.get('password', None)
    user = authenticate(username=username, password=password)
    error = {}
    if not username:
        error = {'username': 'empty'}
    elif not password:
        error = {'password': 'empty'}
    elif not User.objects.filter(username=username).exists():
        error = {'username': 'nonexistent'}
    elif user is None:
        error = {'password': 'wrong'}
    return JsonResponse(error)
