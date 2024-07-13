from blogs.permissions import user_is_blog_owner
from blogs.shortcuts import get_blog_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.utils.extend_schema import extend_schema
from blogs.actions.delete_blog_posts import delete_blog_posts
from blogs.serializers import DeleteBlogPostsFormSerializer
from common.form_serializer import FormSerializer
from blogs.actions.delete_blog_posts import BlogPostsNotFoundError


class DeleteBlogPostsRequestSerializer(FormSerializer):
    delete_blog_posts_form = DeleteBlogPostsFormSerializer()


class DeleteBlogPostsApiView(APIView):
    @extend_schema(
        request=DeleteBlogPostsRequestSerializer,
        responses={
            204: None,
        },
        data=dict(
            blog=get_blog_or_404,
        ),
        permissions=[
            (
                403,
                user_is_blog_owner,
                "You must be the blog owner to delete blog posts.",
            ),
        ],
    )
    def post(self, request, request_data, blog):
        try:
            deleted_count = delete_blog_posts(
                request_data.delete_blog_posts_form, blog=blog
            )
        except BlogPostsNotFoundError as e:
            return Response(
                {"detail": f"One or more blog posts were not found: {e.missing_ids}"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(
            {"deleted_count": deleted_count}, status=status.HTTP_204_NO_CONTENT
        )
