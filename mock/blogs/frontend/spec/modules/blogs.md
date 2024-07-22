1 Types

1.1 Type: Blog

- id: UUID
- name: str
- description: Optional[str]

1.2 Type: BlogPost

- id: UUID
- blog: Blog
- title: str
- isPublished: bool
- content: Optional[str]

2 Mutations

2.1 Mutation: createBlogPost

Arguments:

- createBlogPostForm: Form

2.2 Mutation: deleteBlogPosts

Arguments:

- deleteBlogPostsForm: Form
- blog: Blog

3 Queries

2.1 Query: getBlogs

2.2 Query: getBlogPosts

4 States

4.1 State: BlogsState

Containers:
BlogsCtr:
Facets: - data - selection - highlight

4.2 State: BlogPostsState

Containers:
BlogPostsCtr:
Facets: - data - addition - deletion - display - dragAndDrop - edit - filtering - highlight - insertion - selection

5 Routes

5.1 Route: BlogsPage

5.2 Route: CreateBlogPage

6 StateProviders

6.1 StateProvider: BlogsStateProvider

6.2 StateProvider: BlogPostsStateProvider

7 Views

7.1 View: BlogPage

7.2 View: BlogPostFormView

7.3 View: BlogListView

7.4 View: BlogPostListView

8 Effects

8.1 Effect: SelectBlogEffect

9 Components

9.1 Component: DialogButton

Props:

- trim

9.2 Component: ToolButton

Props:

- trim
