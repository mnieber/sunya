from blogs.actions.create_blog import CreateBlogForm
from blogs.actions.create_blog_post import CreateBlogPostForm
from blogs.models import Blog, BlogPost
from blogs.actions.update_blog_post import UpdateBlogPostForm
from common.form_serializer import FormSerializer
from common.serializers import BaseModelSerializer, ReadSerializerMixin
from blogs.actions.delete_blog_posts import DeleteBlogPostsForm
from common.form_serializer import FormSerializer


class CreateBlogFormSerializer(FormSerializer):
    class Meta:
        form_class = CreateBlogForm


class CreateBlogPostFormSerializer(FormSerializer):
    class Meta:
        form_class = CreateBlogPostForm


class UpdateBlogPostFormSerializer(FormSerializer):
    class Meta:
        form_class = UpdateBlogPostForm


class BlogSerializer(ReadSerializerMixin, BaseModelSerializer):
    class Meta:
        model = Blog
        fields = ["id", "name", "slug", "description", "owner_id", "audience"]


class BlogPostSerializer(ReadSerializerMixin, BaseModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id", "title", "slug", "blog_id", "content"]


class DeleteBlogPostsFormSerializer(FormSerializer):
    class Meta:
        form_class = DeleteBlogPostsForm
