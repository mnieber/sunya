1 Models

1.1 Model: Blog

- id: UUID
- name: str
- description: Optional[str]

1.2 Model: BlogPost

- id: UUID
- blog: Blog
- title: str
- content: Optional[str]

2 Enums

2.1 Enum: BlogAudiences

Items:
- expert
- novice
- any

3 Actions

3.1 Action: create_blog

Arguments:
- create_blog_form: Form

3.2 Action: create_blog_post

Arguments:
- create_blog_post_form: Form
- blog: Blog

3.3 Action: update_blog

Arguments:
- update_blog_form: Form
- blog: Blog

4 Api views

4.1 Api view: CreateBlog

Filters:
-

4.2 Api view: CreateBlogPost

Filters:
-

4.3 Api view: UpdateBlog

Filters:
-


