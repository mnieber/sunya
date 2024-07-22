Scenario: a-user-creates-a-blog-post (backend/ms2_a_user_creates_a_blog_post.md)



# The [alice@example.com+:user] visits the [blogs+:route]




# The [alice@example.com+:user] submits a form to create a [my-blog-post+:blog-post] in the [my-original-blog+:blog]

After this step, the following actors will have been created with the following values:

my-blog-post+:blog-post:
blog=my-original-blog+:blog
content=Hello people
id=691f5870d7a1588290e2e812267710ad
title=My Blog Post

## The [:frontend] makes a [create-blog-post:request] to the [create-blog:api-view]

### The [create-blog:api-view] calls the [create-blog:action] with the [create-blog-post-:form] to create the [my-blog-post+:blog-post]

After this step, the following actors will have been created with the following values:

my-blog-post+:blog-post:
blog=my-original-blog+:blog
content=Hello people
id=691f5870d7a1588290e2e812267710ad
title=My Blog Post


