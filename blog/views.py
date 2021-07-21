"""Blog views."""

# Django
from django.shortcuts import render

# Models
from blog.models import Post, CategoryBlog


def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})


def category(request, category_id):
    category = CategoryBlog.objects.get(id=category_id)
    posts = Post.objects.filter(categories=category)
    return render(request, "blog/category.html", {"category": category, "posts": posts })