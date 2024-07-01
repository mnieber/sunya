from blogs.actions.create_blog import CreateBlogForm
from blogs.actions.create_blog_post import CreateBlogPostForm
from blogs.models import Blog, BlogPost

from common.form_serializer import FormSerializer
from common.serializers import BaseModelSerializer, ReadSerializerMixin


class CreateBlogFormSerializer(FormSerializer):
    class Meta:
        model = CreateBlogForm


class CreateBlogPostFormSerializer(FormSerializer):
    class Meta:
        model = CreateBlogPostForm


class BlogSerializer(ReadSerializerMixin, BaseModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class BlogPostSerializer(ReadSerializerMixin, BaseModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"
