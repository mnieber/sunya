

import mock.blogs.frontend.namespace as F


def resolve_entity_in_global_namespace(name):
    # frontend.Blogs
    if name == "create_blog_mutation":
        return F.Blogs.Mutations.CreateBlog()
    if name == "create_blog_post_mutation":
        return F.Blogs.Mutations.CreateBlogPost()
    if name == "blogs_route":
        return F.Blogs.Routes.Blogs()
    if name == "blog_route":
        return F.Blogs.Routes.Blog()
    if name == "blog_list_view":
        return F.Blogs.Views.BlogListView()
    if name == "blog_form_view":
        return F.Blogs.Views.BlogFormView()
    if name == "blog_post_form_view":
        return F.Blogs.Views.BlogPostFormView()
    if name == "create_blog_button":
        return F.Blogs.Components.CreateBlogButton()
    if name == "create_blog_post_button":
        return F.Blogs.Components.CreateBlogPostButton()

    return None
