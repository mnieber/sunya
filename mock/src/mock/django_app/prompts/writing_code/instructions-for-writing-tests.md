# Instructions for writing tests

When writing tests for an action, please follow the example in blogs/tests/actions/create_blog_post/test_create_blog_post_action.py.

When writing tests for an api-view, please follow the example in blogs/tests/views/create_blog_post_api_view/test_create_blog_post_api_view.py. As shown in the example, the test should use the checks_permission function to verify that the api-view is configured with the correct permission checks.

Note that if the api-view calls an action, then generally we don't need to test that the api-view handles all exceptions that the action may raise. Since the test for the action already verifies that we are validating the inputs, we don't need to test for these conditions again in the test for the api-view, as this would bloat the test code too much.

When writing tests for a permissions.py file, please follow the example in blogs/tests/permissions/test_user_is_blog_owner_permission.py.
