import deepdiff
import pytest
from blogs.permissions import user_is_blog_owner
from blogs.tests.factories import BlogFactory
from blogs.views.create_blog_post_api_view import CreateBlogPostApiView
from django.urls import reverse
from rest_framework.test import APIClient

from api.utils.extend_schema.permissions import checks_permission
from common.utils.test_utils import DeepDiffOperator, rhs_is_not_none
from users.tests.factories import UserFactory


class TestCreateBlogPostApiView:
    @pytest.fixture()
    def client(self):
        client = APIClient()
        return client

    @pytest.fixture()
    def blog_owner(self):
        return UserFactory()

    @pytest.fixture()
    def blog(self, blog_owner):
        return BlogFactory(owner=blog_owner)

    @pytest.mark.django_db()
    def test_create_blog_post_api_view_success(self, client, blog_owner, blog):
        # Given
        client.force_authenticate(user=blog_owner)
        url = reverse("create-blog-post", kwargs=dict(blog_id=blog.id))

        # When
        response = client.post(
            url,
            data=dict(
                create_blog_post_form=dict(
                    title="My blog title",
                    content="My blog content",
                )
            ),
        )

        # Then
        assert response.status_code == 201

        result = response.json()
        diff = deepdiff.DeepDiff(
            {
                "id": "some id",
                "blog_id": str(blog.id),
                "title": "My blog title",
                "content": "My blog content",
            },
            result,
            custom_operators=[
                DeepDiffOperator(rhs_is_not_none, "id"),
            ],
        )
        assert not diff, f"JSON response differs: {diff.pretty()}"

    def test_create_blog_post_api_view_permissions(self):
        assert checks_permission(CreateBlogPostApiView.post, user_is_blog_owner)
