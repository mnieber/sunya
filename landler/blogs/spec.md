0 SPEC comments.

This module specification section contains comments that start with the 'SPEC' keyword.
These comments are meant to guide the source code generation process. They are not part of the actual spec.

1 Models

1.1 Model: Blog

A Django model that represents a blog

Fields:
id: UUID
name: str
owner: User
description: Optional[str]
blog_posts: List[BlogPost]

1.2 Model: BlogPost

A Django model that contains a blog-post

Fields:
id: UUID
blog: Blog
title: str
content: Optional[str]

2 Actions

2.1 Action: CreateBlog

Arguments:
create_blog_form: Form

2.2 Action: CreateBlogPost

Arguments:
create_blog_post_form: Form
blog: Blog

3 API Views

3.1 API View: CreateBlogApiView

3.2 API View: CreateBlogPostApiView

4 Scenarios

SPEC: This section describes scenarios that the module must support. It mentions actors (i.e. the
objects in the scenario) that are based on the data-types in the `spec.md` file of this and
other modules.

SPEC: The actors are described using a special notation: [(actor name+)(actor sub-type):actor-type].
For example:

- the notation `hello-world+:blog-post` means that the type is `blog-post` and the name is `hello-world`.
- the notation `wow+special:blog-post` means that the type is `special:blog-post` and the name is `wow`.

4.1 Scenario: A user creates a blog

```
# The [:frontend] calls the [create-blog:api-view]

## The [create-blog:api-view] calls the [create-blog:action] to create a [my-blog+:blog]

The following actors are created in this step:

[my-blog+:blog]:
id=313828d7-c8db-5139-b89e-d37faf9d6b52
name=my blog
description=My personal blog
blog_posts=[]

### The [create-blog-post:action] validates the name of the [my-blog+:blog-post]

4.2 Scenario: A user creates a blog-post

```

# The [:frontend] calls the [create-blog-post:api-view]

## The [create-blog-post:api-view] calls the [create-blog-post:action] to create a [hello-world+:blog-post]

The following actors are created in this step:

[hello-world+:blog-post]:
name=hello world
content=Hello world, this is my first blog post
blog_id=313828d7-c8db-5139-b89e-d37faf9d6b52

The following actors are updated in this step:

[my-blog+:blog]:
blog_posts=[hello-world+:blog-post]
