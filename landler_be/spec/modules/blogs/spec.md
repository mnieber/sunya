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

2 Enums

2.1 Enum: Audiences

Items:
expert
novice
any

3 Actions

3.1 Action: create_blog

Arguments:
create_blog_form: Form

3.2 Action: create_blog_post

Arguments:
create_blog_post_form: Form
blog: Blog

4 API Views

4.1 API View: CreateBlogApiView

4.2 API View: CreateBlogPostApiView
