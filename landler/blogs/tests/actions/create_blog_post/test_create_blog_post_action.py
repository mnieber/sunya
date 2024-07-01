import pytest
from blogs.actions.create_blog_post import (
    BlogPostWithTitleAlreadyExistsError,
    CreateBlogPostForm,
    create_blog_post,
)
from blogs.tests.factories import BlogFactory, BlogPostFactory

from users.tests.factories import UserFactory


class TestCreateBlogPostAction:
    @pytest.fixture()
    def blog_owner(self):
        return UserFactory()

    @pytest.fixture
    def blog(self, blog_owner):
        return BlogFactory(owner=blog_owner)

    @pytest.mark.django_db
    def test_create_blog_post_success(self, blog):
        # Given
        create_blog_post_form = CreateBlogPostForm(
            title="Test BlogPost", content="A test blog post"
        )

        # When
        blog_post = create_blog_post(create_blog_post_form, blog=blog)

        # Then
        assert blog_post.title == "Test BlogPost"
        assert blog_post.content == "A test blog post"

    @pytest.mark.django_db
    def test_create_blog_post_with_existing_title(self, blog):
        # Given
        BlogPostFactory(title="Existing BlogPost", blog=blog)

        create_blog_post_form = CreateBlogPostForm(
            title="Existing BlogPost", content="A test blog post"
        )

        # When / Then
        with pytest.raises(BlogPostWithTitleAlreadyExistsError):
            create_blog_post(create_blog_post_form, blog=blog)
