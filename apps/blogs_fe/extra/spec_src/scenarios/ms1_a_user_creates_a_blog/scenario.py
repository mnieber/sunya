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


scenario = sunya.add_scenario("ms1_a_user_creates_a_blog")
markdown_node = sunya.add_markdown_node(scenario, "A user creates a blog")

markdown_node.markdown = f"""
```mermaid
sequenceDiagram
    {participant(m.External.Actors.User, role=r.User)}
    {participant(m.Blogs.Views.BlogListView, role=r.BlogListView)}
    {participant(m.Blogs.Views.BlogFormView, role=r.BlogFormView)}
    {participant(m.Blogs.Mutations.CreateBlogMutation, role=r.CreateBlogMutation)}

    # 🔳 Create Blog
    {note_over(r.User, goal(rel().create_a(r.blog).for_the(r.user)))}
    {r.User           >  r.BlogListView}        : {a.it(rel().visits_the(r.blogs_route))}
    {r.BlogListView   >> r.User}                : {a.it(rel().shows(r.create_blog_button))}
    {r.User           >  r.BlogFormView}        : {a.it(rel().presses(r.create_blog_button))}
    {r.User           >> r.BlogFormView}        : {a.it(rel().submits(r.blog_form))}
    {r.BlogFormView   >> r.CreateBlogMutation}  : {a.calls(r.blog_form_data)}
    {r.CreateBlogMutation >> self()}            : {a.creates(r.blog)}
    {r.CreateBlogMutation >> r.BlogFormView}    : {a.returns(r.blog)}
```
"""
