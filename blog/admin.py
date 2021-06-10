"""Blog Admin."""

# Django
from django.contrib import admin
from .models import CategoryBlog, Post

# Models
from .models import CategoryBlog, Post


class CategoryBlogAdmin(admin.ModelAdmin):
    """CategoryBlogAdmin model."""

    readonly_fields=("created", "modified")


class PostAdmin(admin.ModelAdmin):
    """PostAdmin model"""

    readonly_fields=("created", "modified")
 

admin.site.register(CategoryBlog, CategoryBlogAdmin)
admin.site.register(Post, PostAdmin)  