from django.db import models
from django.contrib.auth.models import User
import uuid

from django.urls.base import reverse
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=30, blank=True, null=True)
    intro = models.CharField(max_length=300, blank=True, null=True)
    pic = models.ImageField(upload_to='profiles/', default='profiles/default.jpg')


class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        return super().save(*args, **kwargs)


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    title_image = models.ImageField(upload_to='blog/title_images', null=True, blank=True)
    description = models.CharField(max_length=225)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='likes')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.id}: {self.title}'

    def likes_count(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.pk})

    # an example for custom tags/filters (get model method values with a parameter)
    # def author_status(self, user_id):
    #     if user_id < 10:
    #         return 'VIP Member'
    #     return 'Normal Member'


class Comment(MPTTModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='comments')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ('created_at',)

    def __str__(self):
        return f'A comment authored by {self.author.first_name} {self.author.last_name} at {self.created_at}'

# TODO tags
# TODO multiple form fields with one submit button
# TODO profile picture
# TODO BlogFile model  Image, PDF, maybe videos
# TODO search        
