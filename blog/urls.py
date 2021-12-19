from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/contact/', views.contact, name='contact'),
    path('blog/about/', views.about, name='about'),
    path('blog/blog_list/', views.BlogList.as_view(), name='blog_list'),
    path('author/<str:username>/', views.AuthorBlogList.as_view(), name='author_blog_list'),
    path('category/<str:slug>/', views.CategoryBlogList.as_view(), name='category_blog_list'),
    # path('blog/<int:pk>/', views.BlogDetail.as_view(), name='blog_detail'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),

    # Ajax functions
    path('like_unlike/', views.like_unlike, name='like_unlike'),
    path('register_check/', views.register_check, name='register_check'),
    path('login_check/', views.login_check, name='login_check'),

    # Authentication
    path('accounts/login/', views.UserLoginView.as_view(template_name='blog/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', views.UserCreateView.as_view(), name='register'),

    # Blog CRUD
    path('blog/new/', views.BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/update/', views.BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog_delete'),
]
