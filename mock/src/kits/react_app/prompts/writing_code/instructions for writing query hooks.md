# Instructions for writing query hooks

When writing an query hook file, please follow the example in api/queries/useGetBlogPosts.ts.

## The get function

The post function automatically converts the keys in the response-data from camel-case to snake-case.

## OptionsT

Depending on the use-case, the query hook may need to have a options argument with an `enabled` flag. This is typically the case when the query can only run when some other resource (in the example code this is the blog resource) has been loaded.
