Scenario: a-user-creates-a-blog (backend/ms1_a_user_creates_a_blog.md)



# The [alice@example.com+:user] visits the [http://blogsmanager.io/blogs/create+:page] to create a [my-personal-blog+:blog]




# The [alice@example.com+:user] submits a form to create a [my-personal-blog+:blog]

After this step, the following actors will have been created with the following values:

my-personal-blog+:blog:
description=Random things that interest me
id=110c5658efe54902aabd068ced966b2f
name=My Personal Blog

## The [:frontend] makes a [/api/accounts/sign-up/:request] to the [create-blog:api-view]

### The [create-blog:api-view] calls the [create-blog:action] with the [create-blog-:form] to create a [my-personal-blog+:blog]

After this step, the following actors will have been created with the following values:

my-personal-blog+:blog:
description=Random things that interest me
id=110c5658efe54902aabd068ced966b2f
name=My Personal Blog

#### The [create-blog:action] creates the [my-personal-blog+:blog]

After this step, the following actors will have been created with the following values:

my-personal-blog+:blog:
description=Random things that interest me
id=110c5658efe54902aabd068ced966b2f
name=My Personal Blog


