Scenario: a-user-edits-a-blog (backend/ms3_a_user_edits_a_blog.md)



# The [alice@example.com+:user] visits the [http://blogsmanager.io/blogs/{blog_id}/edit+:page] to edit the [updated-blog-name+:blog]




# The [alice@example.com+:user] submits a form to edit the [updated-blog-name+:blog]

After this step, the following actors will have been created with the following values:

updated-blog-name+:blog:
description=Updated blog description
id=d5b4a9ce5e594a27b9245c437f376e28
name=Updated Blog Name

## The [:frontend] makes a [/api/blogs/d5b4a9ce5e594a27b9245c437f376e28/update/:request] to the [update-blog:api-view]

### The [update-blog:api-view] calls the [update-blog:action] with the [update-blog-:form] to update the [updated-blog-name+:blog]

After this step, the following actors will have been created with the following values:

updated-blog-name+:blog:
description=Updated blog description
id=d5b4a9ce5e594a27b9245c437f376e28
name=Updated Blog Name

#### The [update-blog:action] updates the [updated-blog-name+:blog]

After this step, the following actors will have been created with the following values:

updated-blog-name+:blog:
description=Updated blog description
id=d5b4a9ce5e594a27b9245c437f376e28
name=Updated Blog Name


