Mock components are used as a preparation for creating the real components. In most cases, we won't need a mock component, but if I should ask you to create one, please follow the below guidelines.

# Name and location

The mock component has a name that starts with the word Mock, e.g. MockBlogsPage.
It lives within the code/mocks directory, e.g. mocks/blogs/components/MockBlogsPage.tsx.
It is written in Typescript, but if can use the `any` type to prevent complaints from the typescript compiler.

# Props

The mock component does not use any ContextProps, only normal props.
It uses static data that is created within the same file. A parent mock component may pass this data down to its child mock-components by setting their properties.

# Behaviour

Mock components may simulate behaviour. For example, they may respond to button presses. However, mock components do not actually implement the underlying features, they only simulate the behaviour.

# Rendering and style

Mock components should be written such that they can be rendered directly in the artifact viewer. This makes it easy for me to inspect them and iterate on them. Therefore, all code should be in a single file that exports its main component.

Mock components should use TailwindCSS inline styles. They show light text on a dark background.
Otherwise, please feel free to create your own design and styles.
