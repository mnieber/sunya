from sunya import (
    G as g,
    match_step as match,
)


def implement_step(step):
    if match(step, ("the", g.frontend, "calls_the", g.update_blog_post_mutation)):
        g.blog_post.content = "Hello, World!"
