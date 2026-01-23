import sunya
from sunya import (
    goal,
    R as r,
    M as m,
    Rel as rel,
    actions as a,
    participant,
    note_over,
    self,
)


scenario = sunya.add_scenario("ms3_a_user_updates_a_blog_post")
markdown_node = sunya.add_markdown_node(
    scenario, "A user updates and deletes a blog post"
)

markdown_node.markdown = f"""
```mermaid
sequenceDiagram
    {participant(m.External.Actors.User, role=r.User)}
    {participant(m.Blogs.Views.BlogView, role=r.BlogView)}
    {participant(m.Blogs.Views.BlogPostFormView, role=r.BlogPostFormView)}
    {participant(m.Blogs.Mutations.UpdateBlogPostMutation, role=r.UpdateBlogPostMutation)}
    {participant(m.Blogs.Mutations.DeleteBlogPostsMutation, role=r.DeleteBlogPostsMutation)}

    # 🔳 Edit Blog Post
    {note_over(r.User, goal(rel().edit_a(r.blog_post).in_the(r.blog)))}
    {r.User                   >> r.BlogView}                : {a.it(rel().selects_the(r.blog_post).they_want_to_edit())}
    {r.BlogView               >> r.User}                    : {a.it(rel().shows(r.edit_blog_post_button))}
    {r.User                   >  r.BlogPostFormView}        : {a.it(rel().presses(r.edit_blog_post_button))}
    {r.User                   >> r.BlogPostFormView}        : {a.it(rel().submits(r.blog_post_form))}
    {r.BlogPostFormView       >> r.UpdateBlogPostMutation}  : {a.calls(r.blog_post_form_data)}
    {r.UpdateBlogPostMutation >> self()}                    : {a.it(rel().updates(r.blog_post))}
    {r.UpdateBlogPostMutation >> r.BlogPostFormView}        : {a.returns(r.blog_post)}

    # 🔳 Delete Blog Post
    {note_over(r.User, goal(rel().delete_a(r.blog_post).in_the(r.blog)))}
    {r.User                    >> r.BlogView}                : {a.it(rel().selects_the(r.blog_post).they_want_to_delete())}
    {r.BlogView                >> r.User}                    : {a.it(rel().shows(r.delete_blog_posts_button))}
    {r.User                    >> r.BlogView}                : {a.it(rel().presses(r.delete_blog_posts_button))}
    {r.BlogView                >> r.DeleteBlogPostsMutation} : {a.calls(r.blog_posts)}
    {r.DeleteBlogPostsMutation >> self()}                    : {a.it(rel().deletes(r.blog_posts))}
    {r.DeleteBlogPostsMutation >> r.BlogView}                : {a.returns()}
```
"""
