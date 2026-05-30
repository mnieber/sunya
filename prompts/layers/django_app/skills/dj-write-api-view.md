# Skill: dj-write-api-view

Applies when writing an API view file inside a `views/` subdirectory.

Primary references:
- `blogs_be/src/blogs_be/blogs/views/create_blog_post_api_view.py` (POST view)
- `blogs_be/src/blogs_be/blogs/views/get_blog_posts_api_view.py` (GET view)

---

## File location

```
<module>/views/<action_name>_api_view.py
```

RULE: Each view class lives in its own file. Do not put multiple API views in one file.

## Class structure

Each view file contains one `APIView` subclass with either a `get` or a `post` method (not both).

The `@extend_schema` decorator (from `api.utils.extend_schema`) is placed on the method, not the class.

## `extend_schema` parameters

| Parameter | Purpose |
|-----------|---------|
| `request` | Serializer class describing the POST body (omit for GET views) |
| `responses` | Dict mapping HTTP status code to response serializer |
| `data` | Dict mapping variable names to resolver functions that build the "data spec" |
| `permissions` | List of `(status_code, permission_fn, message)` tuples; use `[]` for public endpoints |

### Data spec (`data=`)

The data spec is resolved incrementally. The runtime starts with a dict that contains:
- All URL path parameters (e.g. `blog_key` from `<str:blog_key>/`)
- `request.user` under the key `"user"`

Each entry in `data=` maps a variable name to a callable that receives the previously resolved variables as keyword arguments. If a resolver raises an exception, `extend_schema` propagates it.

The resolved variables are injected as extra keyword arguments into the view method (e.g. `blog` in `def post(self, request, request_data, blog)`).

### Permissions (`permissions=`)

Each entry is a 3-tuple: `(http_status_code, permission_fn, error_message)`.

Permission functions receive arguments from the data spec — the argument names must match keys in the resolved data dict. If the permission check fails, the given HTTP status is returned with the error message.

## POST view pattern

```python
from blogs.actions.create_blog_post import (
    BlogPostWithTitleAlreadyExistsError,
    create_blog_post,
)
from blogs.permissions import user_is_blog_owner
from blogs.serializers import BlogPostSerializer, CreateBlogPostFormSerializer
from blogs.shortcuts import get_blog_or_400
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from api.utils.extend_schema import extend_schema
from common.form_serializer import FormSerializer


class CreateBlogPostRequestSerializer(FormSerializer):
    create_blog_post_form = CreateBlogPostFormSerializer()


class CreateBlogPostApiView(APIView):
    @extend_schema(
        request=CreateBlogPostRequestSerializer,
        responses={200: BlogPostSerializer},
        data=dict(
            blog=get_blog_or_400,
        ),
        permissions=[
            (403, user_is_blog_owner, "You must be the blog owner to create a blog post."),
        ],
    )
    def post(self, request, request_data, blog):
        try:
            blog_post = create_blog_post(
                create_blog_post_form=request_data.create_blog_post_form,
                blog=blog,
            )
        except BlogPostWithTitleAlreadyExistsError:
            raise ValidationError(code="BLOG_POST_TITLE_ALREADY_EXISTS")

        return Response(
            BlogPostSerializer(blog_post).data, status=status.HTTP_201_CREATED
        )
```

RULE: If the action raises an exception, convert it to a `ValidationError` with a string `code` (and optionally `detail`). Do not let action exceptions bubble up unhandled.

RULE: The `request_data` argument (injected by `extend_schema`) holds the deserialized POST body. Access nested form data via attribute access (e.g. `request_data.create_blog_post_form`).

## GET view pattern

```python
class GetBlogPostsApiView(APIView):
    @extend_schema(
        responses={200: BlogPostSerializer(many=True)},
        data=dict(blog=get_blog_or_400),
        permissions=[],
    )
    def get(self, request, blog):
        blog_posts = BlogPost.objects.filter(blog=blog)
        return Response(BlogPostSerializer(blog_posts, many=True).data, status=status.HTTP_200_OK)
```

## Checklist

- [ ] One view class per file, in `<module>/views/`
- [ ] `@extend_schema` on the method, not the class
- [ ] `data=` dict maps variable names to resolver functions
- [ ] `permissions=` list is present (empty list `[]` for public endpoints)
- [ ] POST: action exceptions caught and re-raised as `ValidationError(code=...)`
- [ ] POST: `request_data` used to access deserialized form fields
- [ ] Response uses the appropriate `status.HTTP_*` constant
