"""Blog Models."""

# Django
from django.db import models
from django.contrib.auth.models import User

# Utilities
from util.models import OnlineStoreModel


class CategoryBlog(OnlineStoreModel):
    """CategoryBlog model."""

    name = models.CharField(max_length=50)
    
    class Meta(OnlineStoreModel.Meta):
        """Meta options."""
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        """Return name's category."""
        return self.name


class Post(OnlineStoreModel):
    """Post model."""

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(CategoryBlog)

    class Meta:
        """Meta options."""
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        """Return title's post"""
        return self.title