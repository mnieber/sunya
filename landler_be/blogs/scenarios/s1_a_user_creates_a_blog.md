Scenario: A user creates a blog

# The [:frontend] calls the [create-blog:api-view]

## The [create-blog:api-view] calls the [create-blog:action] to create a [my-blog+:blog]

The following actors are created in this step:

[my-blog+:blog]
id=313828d7-c8db-5139-b89e-d37faf9d6b52
name=my blog
description=My personal blog
audience=any
blog_posts=[]

### The [create-blog-post:action] validates the name of the [my-blog+:blog-post]
