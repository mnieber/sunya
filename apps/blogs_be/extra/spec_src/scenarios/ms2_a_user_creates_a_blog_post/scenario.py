import sunya
from sunya import (
    R as r,
    M as m,
    Rel as rel,
    goal,
    actions as a,
    it,
    participant,
    note_over,
    self,
)


scenario = sunya.add_scenario("ms2_a_user_creates_a_blog_post")
markdown_node = sunya.add_markdown_node(scenario, "A user creates a blog post")

markdown_node.markdown = f"""
```mermaid
sequenceDiagram
    {participant(m.External.Actors.Frontend, role=r.Frontend)}
    {participant(m.Blogs.ApiViews.CreateBlogPostApiView, role=r.CreateBlogPostApiView)}
    {participant(m.Blogs.Actions.CreateBlogPost, role=r.CreateBlogPostAction)}
    {participant(m.Blogs.Rules.HasForbiddenWords, role=r.HasForbiddenWordsRule)}

    # 🔳 Create Blog Post
    {note_over(r.Frontend, goal(rel().create_a(r.blog_post).in_the(r.blog)))}
    {(r.Frontend               >> r.CreateBlogPostApiView)   - a.calls()}
    {(r.CreateBlogPostApiView  >> r.CreateBlogPostAction)    - a.calls(r.create_blog_post_form)}
    {(r.CreateBlogPostAction   >> r.HasForbiddenWordsRule)   - it().runs(r.blog_post)}
    {(r.HasForbiddenWordsRule  >> r.CreateBlogPostAction)    - a.returns()}
    {(r.CreateBlogPostAction   >> self())                    - a.creates(r.blog_post)}
    {(r.CreateBlogPostAction   >> r.CreateBlogPostApiView)   - a.returns(r.blog_post)}
```
"""
