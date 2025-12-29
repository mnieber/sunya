from kits.django_app.impl.namespace import DjangoModule
import typing as T

from sunya import RelatedSet, Entity, FK


class Blogs(DjangoModule):
    class Models:
        class Blog(Entity):
            name: str
            description: T.Optional[str]
            audience: str = "Audiences: expert | novice | any"
            blog_posts: RelatedSet["Blogs.Models.BlogPost"] = []

        class BlogPost(Entity):
            title: str
            content: T.Optional[str]
            blog: FK["Blogs.Models.Blog"]

    class DomainEvents:
        class BlogCreated:
            pass

        class BlogPostCreated:
            pass
