from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, Blog, Comment

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Comment, MPTTModelAdmin)
