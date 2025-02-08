import mock.blogs.frontend.namespace as F
from sunya import (
    R as r,
    G as g,
    match_step as match,
)


def implement_step(step):
    if match(step, ("the", g.frontend, "calls_the", g.create_blog_post_mutation)):
        r.blog_post = F.Blogs.Types.BlogPost(
            title="My First Blog Post",
            content="Hello",
            level="novice",
            _blog=g.blog,
        )
