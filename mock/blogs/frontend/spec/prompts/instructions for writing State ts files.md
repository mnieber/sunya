# Instructions for writing State.ts files

When writing a State.ts file, please follow the example in blogPosts/BlogPostsState/BlogPostsState.ts.

## Purpose of the State class

A state class stores a resource, and various type of meta-information on that resource such as its selection-state, drag-and-drop-state, etc. The resource, together with this meta-information is stored in a container object inside of the state. Sometimes there is more than one container in the state.

Each type of meta-information in the container is called a facet. In the sample code, there is a selection-facet, a deletion-facet, etc. The spec file will indicate per State which facets are required. However, if the scenarios require facets that are not listed in the spec, then please let me know.

## The Data facet

Usually the data that a container stores and operates on requires a custom Data facet. In the sample code this is the BlogPostsData class. It is located in the directory that also contains the State class.

## The registerCtr function

The state calls a registerCtr function to map the output of certain facets to the inputs of other facets. Moreover, the registerCtr function registers call-back actions that must happen when some facet-operations (such as deletion.delete()) happen.

## The props object

The State class takes a props object that contains hook functions that are used to connect the State to the outside world. In the example code, the props object contains a getBlogPosts function that returns the list of blog-posts that will be stored in the data facet. It also contains a deleteBlogPosts function that will be called in the callback that is installed for the deletion.delete operation.

## The actionsCtr object

Using container classes and facets to provide an interface for querying and manipulating a resource generally works well but can be overkill in some cases. For example, to allow marking a blog-post as published we could introduce a new facet such as "publishing", but it's simpler to add a markPublicationAsPublished action to the State class. This is the purpose of the actionsCtr object. It exposes a set of functions that directly manipulate a resource. Generally, either the spec file or the code generation instructions will make it clear whether a facet or an action should be used to expose a particular functionality.

If an action function is not simple enough be be inlined in the actionCtr object, then it should use a function such as `reformatBlogPost` that comes from a lib file such as /src/blogPosts/lib/reformatBlogPost.ts.

If the State class doesn't need an actionsCtr object, then please omit it.
