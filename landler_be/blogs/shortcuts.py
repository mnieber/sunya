from blogs.models import Blog
from rest_framework.generics import get_object_or_404
from common.utils.ids import is_uuid


def get_blog_or_404(blog_key):
    kwargs = {}
    if is_uuid(blog_key):
        kwargs["pk"] = blog_key
    else:
        kwargs["slug"] = blog_key
    return get_object_or_404(Blog, **kwargs)
