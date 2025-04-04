# Instructions for writing model type files

When writing a model type file, please follow the example in api/types/BlogPostT.ts.

## The T suffix

All pure typescript types have a T as their suffix. For example, the type for the BlogPost model has the name BlogPostT.

## The EntityT type

The EntityT type is a mixin that adds an id field.

## The create function (createBlogPost)

Each type wil have a create function that creates a transient instance of that type. The initRS function is used to initialize the so-called resource-state of the object, which is used to track whether the resource is updating or reloading.
