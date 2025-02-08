import mock.blogs.backend.namespace as B
from sunya import (
    R as r,
    match_step as match,
)


def implement_step(step):
    if match(step, ("create_a", r.blog_post, "in_the", r.blog)):
        r.blog_post = B.Blogs.Models.BlogPost(
            title="My Blog Post",
            content="Hello people",
            _blog=r.blog,
        )
