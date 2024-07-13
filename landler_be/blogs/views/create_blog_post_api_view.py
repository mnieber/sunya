from blogs.actions.create_blog_post import (
    BlogPostWithTitleAlreadyExistsError,
    create_blog_post,
)
from blogs.permissions import user_is_blog_owner
from blogs.serializers import BlogPostSerializer, CreateBlogPostFormSerializer
from blogs.shortcuts import get_blog_or_404
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
        responses={
            200: BlogPostSerializer,
        },
        data=dict(
            blog=get_blog_or_404,
        ),
        permissions=[
            (
                403,
                user_is_blog_owner,
                "You must be the blog owner to create a blog post.",
            ),
        ],
    )
    def post(self, request, request_data, blog):
        try:
            blog_post = create_blog_post(
                create_blog_post_form=request_data.create_blog_post_form,
                blog=blog,
            )
        except BlogPostWithTitleAlreadyExistsError:
            raise ValidationError(
                {
                    "non_field_errors": [
                        _(
                            "A blog post with this title has already been created in this blog."
                        )
                    ],
                }
            )

        return Response(
            BlogPostSerializer(blog_post).data, status=status.HTTP_201_CREATED
        )
