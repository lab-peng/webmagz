from blog.models import Category, Blog


def contexts(request):
    categories = Category.objects.all()
    recent_posts = Blog.objects.all()[0:4]
    recent_post = Blog.objects.all()[0]
    # print(request.method)
    context = {
        'categories': categories,
        'recent_posts': recent_posts,
        'recent_post': recent_post,
    }
    return context
