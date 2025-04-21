import mock.blogs.frontend.namespace as F
from sunya import (
    R as r,
    G as g,
    match_step as match,
)


def implement_step(step):
    if match(step, ("create_a", r.blog, "for_the", r.user)):
        r.user = F.Users.Types.User(email="alice@example.com")

    if match(step, ("the", g.frontend, "calls_the", g.create_blog_mutation)):
        r.blog = F.Blogs.Types.Blog(
            name="My Personal Blog",
            description="Random things that interest me",
        )
