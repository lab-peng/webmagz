from blog.models import Category, Blog


def contexts(request):
    categories = Category.objects.all()
    recent_posts = Blog.objects.filter(pk__in=[1, 2, 3, 4])
    recent_post = Blog.objects.first()
    # print(request.method)
    context = {
        'categories': categories,
        'recent_posts': recent_posts,
        'recent_post': recent_post,
    }
    return context
