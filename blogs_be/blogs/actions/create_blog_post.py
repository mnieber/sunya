import typing as T

from blogs.models import Blog, BlogPost
from dataclassy import dataclass

from common.utils.arg_utils import optional_args


@dataclass
class CreateBlogPostForm:
    title: str
    content: T.Optional[str] = None


def create_blog_post(create_blog_post_form: CreateBlogPostForm, blog: Blog):
    _validate_args(create_blog_post_form, blog)

    blog_post = BlogPost(
        blog=blog,
        title=create_blog_post_form.title,
        **optional_args(content=create_blog_post_form.content)
    )
    blog_post.save()

    return blog_post


def _validate_args(create_blog_post_form: CreateBlogPostForm, blog: Blog):
    if BlogPost.objects.filter(title=create_blog_post_form.title, blog=blog).exists():
        raise BlogPostWithTitleAlreadyExistsError()


class BlogPostWithTitleAlreadyExistsError(Exception):
    pass
