def add_sample_code(file_map, dir_list, sample_code_in):
    sample_code = "instructions/code"
    file_map.update(
        {
            f"{sample_code_in}/actions/create_blog_post.py": f"{sample_code}/actions",
            f"{sample_code_in}/actions/create_blog.py": f"{sample_code}/actions",
            f"{sample_code_in}/admin.py": f"{sample_code}",
            f"{sample_code_in}/enums.py": f"{sample_code}",
            f"{sample_code_in}/models.py": f"{sample_code}",
            f"{sample_code_in}/permissions.py": f"{sample_code}",
            f"{sample_code_in}/serializers.py": f"{sample_code}",
            f"{sample_code_in}/shortcuts.py": f"{sample_code}",
            f"{sample_code_in}/tests/actions/create_blog/*": f"{sample_code}/tests/actions/create_blog",
            f"{sample_code_in}/tests/actions/create_blog_post/*": f"{sample_code}/tests/actions/create_blog_post",
            f"{sample_code_in}/tests/factories.py": f"{sample_code}/tests",
            f"{sample_code_in}/tests/permissions/test_user_is_blog_owner_permission.py": f"{sample_code}/tests/permissions",
            f"{sample_code_in}/tests/views/create_blog_api_view/*": f"{sample_code}/tests/views/create_blog_api_view",
            f"{sample_code_in}/tests/views/create_blog_post_api_view/*": f"{sample_code}/tests/views/create_blog_post_api_view",
            f"{sample_code_in}/urls.py": f"{sample_code}",
            f"{sample_code_in}/views/create_blog_api_view.py": f"{sample_code}/views",
            f"{sample_code_in}/views/create_blog_post_api_view.py": f"{sample_code}/views",
        }
    )
    dir_list += [
        f"{sample_code}",
        f"{sample_code}/actions",
        f"{sample_code}/tests/actions/create_blog",
        f"{sample_code}/tests/actions/create_blog_post",
        f"{sample_code}/tests",
        f"{sample_code}/tests/permissions",
        f"{sample_code}/tests.views/create_blog_api_view",
        f"{sample_code}/tests.views/create_blog_post_api_view",
        f"{sample_code}/views",
    ]
