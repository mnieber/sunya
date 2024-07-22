# Instructions for writing State.ts files

When writing a State.ts file, please follow the example in blogPosts/BlogPostsState/BlogPostsState.ts.

## Purpose of the State class

A state class stores a resource, and various type of meta-information on that resource such as its selection-state, drag-and-drop-state, etc. The resource, together with this meta-information is stored in a container object inside of the state. Sometimes there is more than one container in the state.

Each type of meta-information in the container is called a facet. In the sample code, there is a selection-facet, a deletion-facet, etc. The spec file will indicate per State which facets are required. However, if the scenarios require facets that are not listed in the spec, then please let me know.

## The register-container function

The state calls a register-container function to map the output of certain facets to the inputs of other facets. Moreover, the register-container function registers call-back actions that must happen when some facet-operations (such as deletion.delete()) happen.

## The props object

The State class takes a props object that contains hook functions that are used to connect the State to the outside world. In the example code, the props object contains a getBlogPosts function that returns the list of blog-posts that will be stored in the data facet. It also contains a deleteBlogPosts function that will be called in the callback that is installed for the deletion.delete operation.
