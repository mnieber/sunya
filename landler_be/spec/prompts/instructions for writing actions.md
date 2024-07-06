# Instructions for writing action files

When writing an action file, please follow the example in blogs/actions/create_blog_post.py.

Action files live in the actions sub-directory. An action is a function that changes the application state as required by a particular "role". Here "role" is meant in the context of SRP, for example: the "blog post manager" could conceptually be a role in our system, and the create_blog_post action is responsible to that role. The Django Blog model class is only responsible for exposing the general Blog data, and therefore it does not have a create_blog function.
