from blogs.actions.create_blog import create_blog
from blogs.actions.create_blog_post import BlogPostWithTitleAlreadyExistsError
from blogs.serializers import BlogSerializer, CreateBlogFormSerializer
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from api.utils.extend_schema import extend_schema
from common.form_serializer import FormSerializer


class CreateBlogRequestSerializer(FormSerializer):
    create_blog_form = CreateBlogFormSerializer()


class CreateBlogApiView(APIView):
    @extend_schema(
        request=CreateBlogRequestSerializer,
        responses={
            200: BlogSerializer,
        },
        data=dict(),
        permissions=[],
    )
    def post(self, request, request_data):
        try:
            blog = create_blog(
                create_blog_form=request_data.create_blog_form,
                owner=request.user,
            )
        except BlogPostWithTitleAlreadyExistsError:
            raise ValidationError({"name": "Blog with this name already exists."})

        return Response(BlogSerializer(blog).data, status=status.HTTP_201_CREATED)
