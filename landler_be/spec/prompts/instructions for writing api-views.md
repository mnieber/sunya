# Instructions for writing api-view files

When writing an view file, please follow the example in blogs/views/create_blog_post_api_view.py.

View files live in the views sub-directory. An view file implements a REST api view. It contains an ApiView class that has either a get or a post function.

Every view has associated permissions that are specified in the permissions field of the extend_schema decorator. The permission functions have arguments that are resolved by the data spec in the data argument of extend_schema.

The data spec is resolved by incrementally building a dictionary. The initial dictionary contains all url-parameters that are embedded in the url (in the example of blogs/views/create_blog_post_api_view.py this is the blog_key parameter). Moreover, the value of request.user is added to the dictionary under the "user" key. The data spec contains a mapping from the variable name to the resolution function that resolves that variable. If the variable cannot be resolved then extend_schema will raise an exception.

The body of an api view will first validate the input arguments. If the api view handles a POST request then it will usually call an action to do the actual work. If this action raises an exception then it is converted into a user-friendly error message and returned in the response.
