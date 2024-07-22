Scenario: a-user-creates-a-blog (backend/ms1_a_user_creates_a_blog.md)



# The [alice@example.com+:user] visits the [blogs+:route] to create a [my-personal-blog+:blog]




# The [alice@example.com+:user] submits a form to create a [my-personal-blog+:blog]

After this step, the following actors will have been created with the following values:

my-personal-blog+:blog:
description=Random things that interest me
id=2fc4bd1c19a158c4b0eeb255b9d8a370
name=My Personal Blog

## The [:frontend] makes a [create-blog:request] to the [create-blog:api-view]

### The [create-blog:api-view] calls the [create-blog:action] with the [create-blog-:form] to create a [my-personal-blog+:blog]

After this step, the following actors will have been created with the following values:

my-personal-blog+:blog:
description=Random things that interest me
id=2fc4bd1c19a158c4b0eeb255b9d8a370
name=My Personal Blog

#### The [create-blog:action] creates the [my-personal-blog+:blog]

After this step, the following actors will have been created with the following values:

my-personal-blog+:blog:
description=Random things that interest me
id=2fc4bd1c19a158c4b0eeb255b9d8a370
name=My Personal Blog


