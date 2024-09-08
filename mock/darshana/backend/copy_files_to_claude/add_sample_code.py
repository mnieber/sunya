def add_sample_code(file_map, dir_list, sample_code_in):
    sample_code = "instructions/code"
    file_map.update(
        {
            f"{sample_code_in}/blogs/actions/create_blog_post.py": f"{sample_code}/blogs/actions",
            f"{sample_code_in}/blogs/actions/create_blog.py": f"{sample_code}/blogs/actions",
            f"{sample_code_in}/blogs/admin.py": f"{sample_code}/blogs",
            f"{sample_code_in}/blogs/enums.py": f"{sample_code}/blogs",
            f"{sample_code_in}/blogs/models.py": f"{sample_code}/blogs",
            f"{sample_code_in}/blogs/permissions.py": f"{sample_code}/blogs",
            f"{sample_code_in}/blogs/serializers.py": f"{sample_code}/blogs",
            f"{sample_code_in}/blogs/shortcuts.py": f"{sample_code}/blogs",
            f"{sample_code_in}/blogs/tests/actions/create_blog/*.py": f"{sample_code}/blogs/tests/actions/create_blog",
            f"{sample_code_in}/blogs/tests/actions/create_blog_post/*.py": f"{sample_code}/blogs/tests/actions/create_blog_post",
            f"{sample_code_in}/blogs/tests/factories.py": f"{sample_code}/blogs/tests",
            f"{sample_code_in}/blogs/tests/permissions/test_user_is_blog_owner_permission.py": f"{sample_code}/blogs/tests/permissions",
            f"{sample_code_in}/blogs/tests/views/create_blog_api_view/*.py": f"{sample_code}/blogs/tests/views/create_blog_api_view",
            f"{sample_code_in}/blogs/tests/views/create_blog_post_api_view/*.py": f"{sample_code}/blogs/tests/views/create_blog_post_api_view",
            f"{sample_code_in}/blogs/urls.py": f"{sample_code}/blogs",
            f"{sample_code_in}/blogs/views/create_blog_api_view.py": f"{sample_code}/blogs/views",
            f"{sample_code_in}/blogs/views/create_blog_post_api_view.py": f"{sample_code}/blogs/views",
        }
    )
    dir_list += [
        f"{sample_code}/blogs",
        f"{sample_code}/blogs/actions",
        f"{sample_code}/blogs/tests/actions/create_blog",
        f"{sample_code}/blogs/tests/actions/create_blog_post",
        f"{sample_code}/blogs/tests",
        f"{sample_code}/blogs/tests/permissions",
        f"{sample_code}/blogs/tests/views/create_blog_api_view",
        f"{sample_code}/blogs/tests/views/create_blog_post_api_view",
        f"{sample_code}/blogs/views",
    ]
