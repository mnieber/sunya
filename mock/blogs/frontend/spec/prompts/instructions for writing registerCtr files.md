# Instructions for writing registerCtr files

When writing a registerCtr file, please follow the example in blogPosts/BlogPostsState/registerBlogPostsCtr.ts.

## The mapData function

The mapData function maps the output of certain facets to the inputs of other facets. By looking at the example code, you can see how the facets are wired up. If the set of facets changes, please make a best effort to connect them, but don't worry if you cannot solve this part, as I will be able to correct it later.

### The getBlogPostById function

The sample code shows the use of a getBlogPostById function. In most cases, the mapData function needs this internal helper function to retrieve objects from the Data facet in the container.

### Mapping to selectableIds and highlightableIds

Note that the mappings to `selection.selectableIds` and `highlight.highlightableIds` use ramda. Also note that the mapping to `selection.items` uses the getBlogPostById helper. Since `selection.itemIds` may temporarily contains stale ids, this mapping function filters out any empty results.

## The setCallbacks function

The setCallbacks function registers callback actions that must happen when some facet-operations (such as deletion.delete()) happen. Note that the callback functions use the props object of the related State instance to ensure that the proper external side-effects are executed.
