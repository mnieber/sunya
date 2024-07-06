import pytest
from blogs.tests.factories import BlogFactory
from django.urls import reverse
from rest_framework.test import APIClient

from users.tests.factories import UserFactory


class TestDashboardPlotReport:
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
    def test_create_blog_post_api_view(self, client, blog_owner, blog):
        client.force_authenticate(user=blog_owner)

        url = reverse("create-blog-post", kwargs=dict(blog_id=blog.id))
        response = client.post(
            url,
            data=dict(
                create_blog_post_form=dict(
                    title="string",
                    content="string",
                )
            ),
        )
        result = response.json()
        assert result
        assert response.status_code == 201
