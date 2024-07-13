from blogs.views.create_blog_api_view import CreateBlogApiView
from blogs.views.create_blog_post_api_view import CreateBlogPostApiView
from blogs.views.get_blogs_api_view import GetBlogsApiView
from django.urls import path, re_path
from blogs.views.get_blog_posts_api_view import GetBlogPostsApiView
from blogs.views.delete_blog_posts_api_view import DeleteBlogPostsApiView

urlpatterns = [
    path(
        "<str:blog_key>/blog-posts/",
        CreateBlogPostApiView.as_view(),
        name="create-blog-post",
    ),
    re_path(
        "^$",
        CreateBlogApiView.as_view(),
        name="create-blog",
    ),
    path("list", GetBlogsApiView.as_view(), name="get-blogs"),
    path(
        "<str:blog_key>/blog-posts/list/",
        GetBlogPostsApiView.as_view(),
        name="get-blog-posts",
    ),
    path(
        "<str:blog_key>/blog-posts/delete/",
        DeleteBlogPostsApiView.as_view(),
        name="delete-blog-posts",
    ),
]
