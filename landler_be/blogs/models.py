from django.db import models

from blogs.enums import Audiences
from common.fields import SingleLineTextField
from common.models import BaseModel


class Blog(BaseModel):
    description = models.TextField(blank=True, null=True)
    name = SingleLineTextField()
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="blogs"
    )
    audience = SingleLineTextField(choices=Audiences.choices, default=Audiences.ANY)

    def __str__(self):
        return self.name


class BlogPost(BaseModel):
    blog = models.ForeignKey(
        "blogs.Blog", on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField(blank=True, null=True)
    title = SingleLineTextField()

    def __str__(self):
        return self.title
