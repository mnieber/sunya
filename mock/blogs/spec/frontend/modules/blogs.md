1 Types

1.1 Type: Blog

- id: UUID
- name: str
- description: Optional[str]

1.2 Type: BlogPost

- id: UUID
- blog: Blog
- title: str
- content: Optional[str]

2 Mutations

2.1 Mutation: CreateBlog

Arguments:
- createBlogForm: Form

2.2 Mutation: CreateBlogPost

Arguments:
- createBlogPostForm: Form
- blog: Blog

2.3 Mutation: DeleteBlogPosts

Arguments:
- deleteBlogPostsForm: Form

3 Queries

3.1 Query: GetBlogs


3.2 Query: GetBlogPosts

4 States

4.1 State: BlogsState

Containers:
- BlogsCtr:
    Facets:
    - data
    - selection
    - highlight


4.2 State: BlogPostsState

Containers:
- BlogPostsCtr:
    Facets:
    - data
    - addition
    - deletion
    - display
    - dragAndDrop
    - edit
    - filtering
    - highlight
    - insertion
    - selection

5 Routes

5.1 Route: Blogs


5.2 Route: Blog

6 State-Providers

6.1 State-Provider: BlogsStateProvider


6.2 State-Provider: BlogPostsStateProvider

7 Views

7.1 View: BlogPostFormView


7.2 View: BlogListView


7.3 View: BlogPostListView

8 Effects

8.1 Effect: SelectBlogEffect

9 Components

9.1 Component: DialogButton


9.2 Component: ToolButton

