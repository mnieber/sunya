Scenario: A user creates a blog-post

# The [:frontend] calls the [create-blog-post:api-view]

## The [create-blog-post:api-view] calls the [create-blog-post:action] to create a [hello-world+:blog-post]

The following actors are created in this step:

[hello-world+:blog-post]
name=hello world
content=Hello world, this is my first blog post
blog=my-blog+:blog

The following actors are updated in this step:

[my-blog+:blog]
blog_posts=[hello-world+:blog-post]
