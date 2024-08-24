Mock components are used as a preparation for creating the real components. The features of a mock component are the following:

- it has a name that starts with the word Mock, e.g. MockBlogsPage
- it lives within the code/mocks directory, e.g. mocks/blogs/components/MockBlogsPage.tsx
- it does not use any ContextProps, only normal props
- a mock component can contain other child mock-components
- mock components use static data that is created within the same file. A parent mock component may pass this data down to its child mock-components by setting their properties
- mock components may simulate behaviour. For example, they may respond to button presses. However, mock components do not actually implement the underlying features, they only simulate the behaviour.
- mock components should be written such that they can be rendered directly in the artifact viewer. This makes it easy for me to inspect them and iterate on them. Therefore, all code should be in a single file that has a default export.

In most cases, we won't need a mock component, but if I should ask you to create one, please follow the above guidelines.
