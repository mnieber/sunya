# Instructions for writing mutation hooks

When writing an mutation hook file, please follow the example in api/mutations/useCreateBlogPost.ts.

## useObservableMutation

A mutation hook will use useObservableMutation to wrap the result of an async request in a MobX-observable ObservableMutation object that has an API that is similar to the one from tanstack-query.

## The post function

The post function automatically converts the keys in the post-data from camel-case to snake-case.
