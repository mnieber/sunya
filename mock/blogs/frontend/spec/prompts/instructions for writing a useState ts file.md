# Instructions for writing a useState.ts file

When writing a useState.ts file, please follow the example in blogPosts/hooks/useBlogPostState.ts.

## The tracking of resource states

The state of a resource is tracked by adding a ResourceState object to the resource (using a Symbol as the key). The state-provider will install so-called "updating-sources" and "loading-sources" in the ResourceState. An updating-source is a function that returns true if the resource is currently updating. Similarly, a load-source is a function that returns true if the resource is currently loading. This allows for a lot of flexibility in deciding if a resource is currently loading or updating. For example, the code may adding a load-source that returns true based on the resource-state of some other resource. For example, this allows you to specify that resource A is updating if resource B is loading.

### The graftResourceStatesFromMemo function

The resources are freshly fetched from the server they do not yet have a resource-state. However, the stale resource does have one, and we don't want to throw it away (because it should still be used to inform us about the resource state of the fresh resource). For example, suppose that a blog-post A is being deleted, but at the same time the blog-posts are also refreshed. To correctly track the deletion-related state of A, we must copy the resource-state of the stale copy of A to the fresh copy. The graftResourceStatesFromMemo function takes care of this. It stores the current set of resource-states (keyed by the resource id) and passes them to the fresh resources.

### The trackPromise function

The trackPromise function creates a wrapper around a promise. This wrapper adds loading-sources and updating-sources to particular sets of resources based on the state of the promise. In the example code, the resource-state of all blogPosts is set to updating while the deleteBlogPosts mutation is running.
