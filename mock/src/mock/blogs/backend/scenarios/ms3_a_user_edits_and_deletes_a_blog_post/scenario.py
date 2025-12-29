import sunya
from sunya import (
    R as r,
    M as m,
    Rel as rel,
    goal,
    actions as a,
    participant,
    note_over,
    self,
)


scenario = sunya.add_scenario("ms3_a_user_edits_and_deletes_a_blog_post")
markdown_node = sunya.add_markdown_node(
    scenario, "A user edits and deletes a blog post"
)

markdown_node.markdown = f"""
```mermaid
sequenceDiagram
    {participant(m.External.Actors.Frontend, role=r.Frontend)}
    {participant(m.Blogs.ApiViews.UpdateBlogPostApiView, role=r.UpdateBlogPostApiView)}
    {participant(m.Blogs.Actions.UpdateBlogPost, role=r.UpdateBlogPostAction)}
    {participant(m.Blogs.Rules.HasForbiddenWords, role=r.HasForbiddenWordsRule)}
    {participant(m.Blogs.ApiViews.DeleteBlogPostsApiView, role=r.DeleteBlogPostsApiView)}
    {participant(m.Blogs.Actions.DeleteBlogPosts, role=r.DeleteBlogPostsAction)}

    # 🔳 Edit Blog Post
    {note_over(r.Frontend, goal(rel().edit_a(r.blog_post).in_the(r.blog)))}
    {r.Frontend               >> r.UpdateBlogPostApiView}    : {a.calls()}
    {r.UpdateBlogPostApiView  >> r.UpdateBlogPostAction}     : {a.calls(r.update_blog_post_form)}
    {r.UpdateBlogPostAction   >> r.HasForbiddenWordsRule}    : {a.it(rel().runs(r.blog_post))}
    {r.HasForbiddenWordsRule  >> r.UpdateBlogPostAction}     : {a.returns()}
    {r.UpdateBlogPostAction   >> self()}                     : {a.it(rel().updates(r.blog_post))}
    {r.UpdateBlogPostAction   >> r.UpdateBlogPostApiView}    : {a.returns(r.blog_post)}

    # 🔳 Delete Blog Posts
    {note_over(r.Frontend, goal(rel().delete_some(r.blog_posts).in_the(r.blog)))}
    {r.Frontend                >> r.DeleteBlogPostsApiView}   : {a.calls()}
    {r.DeleteBlogPostsApiView  >> r.DeleteBlogPostsAction}    : {a.calls(r.blog_posts)}
    {r.DeleteBlogPostsAction   >> self()}                     : {a.it(rel().deletes(r.blog_posts))}
    {r.DeleteBlogPostsAction   >> r.DeleteBlogPostsApiView}   : {a.returns()}
```
"""
