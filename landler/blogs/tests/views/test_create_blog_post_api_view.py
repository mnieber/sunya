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
        response = client.get(url)
        result = response.json()
        __import__("pudb").set_trace()  # zz
        assert result
        assert response.status_code == 200
