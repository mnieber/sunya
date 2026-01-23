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


scenario = sunya.add_scenario("ms2_a_user_creates_a_blog_post")
markdown_node = sunya.add_markdown_node(scenario, "A user creates a blog post")

markdown_node.markdown = f"""
```mermaid
sequenceDiagram
    {participant(m.External.Actors.User, role=r.User)}
    {participant(m.Blogs.Views.BlogListView, role=r.BlogListView)}
    {participant(m.Blogs.Views.BlogView, role=r.BlogView)}
    {participant(m.Blogs.Views.BlogPostFormView, role=r.BlogPostFormView)}
    {participant(m.Blogs.Mutations.CreateBlogPostMutation, role=r.CreateBlogPostMutation)}

    # 🔳 Create Blog Post
    {note_over(r.User, goal(rel().create_a(r.blog_post).in_the(r.blog)))}
    {r.User                  >  r.BlogListView}           : {a.it(rel().visits_the(r.blogs_route))}
    {r.User                  >  r.BlogView}               : {a.it(rel().clicks_on_a(r.blog).to_visit_the(r.blog_route))}
    {r.BlogView              >> r.User}                   : {a.it(rel().shows(r.create_blog_post_button))}
    {r.User                  >  r.BlogPostFormView}       : {a.it(rel().presses(r.create_blog_post_button))}
    {r.User                  >> r.BlogPostFormView}       : {a.it(rel().submits(r.blog_post_form))}
    {r.BlogPostFormView      >> r.CreateBlogPostMutation} : {a.calls(r.blog_post_form_data)}
    {r.CreateBlogPostMutation >> self()}                  : {a.creates(r.blog_post)}
    {r.CreateBlogPostMutation >> r.BlogPostFormView}      : {a.returns(r.blog_post)}
```
"""
