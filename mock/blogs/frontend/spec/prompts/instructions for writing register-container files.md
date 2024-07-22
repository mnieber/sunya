# Instructions for writing register-container files

When writing a register-container file, please follow the example in blogPosts/BlogPostsState/registerBlogPostsCtr.ts.

## The mapData function

The mapData function maps the output of certain facets to the inputs of other facets. By looking at the example code, you can see how the facets are wired up. If the set of facets changes, please make a best effort to connect them, but don't worry if you cannot solve this part, as I will be able to correct it later.

## The setCallbacks function

The setCallbacks function registers callback actions that must happen when some facet-operations (such as deletion.delete()) happen. Note that the callback functions use the props object of the related State instance to ensure that the proper external side-effects are executed.
