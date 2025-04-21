import mock.blogs.backend.namespace as B


def resolve_entity_in_global_namespace(name):
    if name == "create_blog_action":
        return B.Blogs.Actions.CreateBlog()
    if name == "create_blog_post_action":
        return B.Blogs.Actions.CreateBlogPost()
    if name == "update_blog_action":
        return B.Blogs.Actions.UpdateBlog()
    if name == "create_blog_api_view":
        return B.Blogs.Api.CreateBlogApiView()
    if name == "create_blog_post_api_view":
        return B.Blogs.Api.CreateBlogPostApiView()
    if name == "update_blog_api_view":
        return B.Blogs.Api.UpdateBlogApiView()
    if name == "has_forbidden_words_rule":
        return B.Blogs.Rules.HasForbiddenWords()
    if name == "update_blog_post_action":
        return B.Blogs.Actions.UpdateBlogPost()
    if name == "delete_blog_posts_action":
        return B.Blogs.Actions.DeleteBlogPosts()
    if name == "update_blog_post_api_view":
        return B.Blogs.Api.UpdateBlogPostApiView()
    if name == "delete_blog_posts_api_view":
        return B.Blogs.Api.DeleteBlogPostsApiView()

    return None
