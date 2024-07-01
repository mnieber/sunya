from blogs.views.create_blog_post_api_view import CreateBlogPostApiView
from django.urls import path

urlpatterns = [
    path(
        "blogs/<uuid:blog_id>/blog-posts/",
        CreateBlogPostApiView.as_view(),
        name="create-blog-post",
    )
]
