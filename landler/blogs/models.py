from django.db import models
from rest_framework.generics import get_object_or_404

from common.models import BaseModel


class Blog(BaseModel):
    description = models.TextField(blank=True, null=True)
    name = models.TextField()
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="blogs"
    )

    def __str__(self):
        return self.name


class BlogPost(BaseModel):
    blog = models.ForeignKey(
        "blogs.Blog", on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField(blank=True, null=True)
    title = models.TextField()

    def __str__(self):
        return self.title


def get_blog_or_404(blog_id):
    return get_object_or_404(Blog, pk=blog_id)
