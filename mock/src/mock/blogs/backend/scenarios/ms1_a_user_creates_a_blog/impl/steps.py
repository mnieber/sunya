import mock.blogs.backend.namespace as B
from sunya import R as r, I as i, match_step as match, it


def implement_step(step):
    if match(step, (i.create_a(r.blog).for_the(r.user))):
        r.user = B.Users.Models.User(
            email="alice@example.com",
            password="password",
        )

    elif match(step, it().creates_the(r.blog)):
        r.blog = B.Blogs.Models.Blog(
            name="My Personal Blog",
            description="Random things that interest me",
            audience="any",
        )
        r.user.blogs.append(r.blog)
