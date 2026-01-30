import sunya
from sunya import (
    goal,
    M as m,
    R as r,
    Rel as rel,
    actions as a,
    it,
    participant,
    note_over,
    self,
)

scenario = sunya.add_scenario("ms1_a_user_creates_a_blog")
markdown_node = sunya.add_markdown_node(scenario, "A user creates a blog")

markdown_node.markdown = f"""
```mermaid
sequenceDiagram
    {participant(m.External.Actors.Frontend, role=r.Frontend)}
    {participant(m.Blogs.ApiViews.CreateBlogApiView, role=r.CreateBlogApiView)}
    {participant(m.Blogs.Actions.CreateBlog, role=r.CreateBlogAction)}
    {participant(m.Blogs.Rules.HasForbiddenWords, role=r.HasForbiddenWordsRule)}

    # 🔳 Create Blog
    {note_over(r.Frontend, goal(rel().create_a(r.blog).for_the(r.user)))}
    {(r.Frontend              >> r.CreateBlogApiView)      - a.calls()}
    {(r.CreateBlogApiView     >> r.CreateBlogAction)       - a.calls(r.create_blog_form)}
    {(r.CreateBlogAction      >> r.HasForbiddenWordsRule)  - a.calls()}
    {(r.HasForbiddenWordsRule  >> r.CreateBlogAction)      - a.returns()}
    opt No forbidden words found
    {(r.CreateBlogAction      >> self())                   - a.creates(r.blog)}
    end
    {(r.CreateBlogAction      >> r.CreateBlogApiView)      - a.returns(r.blog)}

```
"""
