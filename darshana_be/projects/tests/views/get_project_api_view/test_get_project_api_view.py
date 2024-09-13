import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from projects.tests.factories import ProjectFactory
from users.tests.factories import UserFactory


class TestGetProjectApiView:
    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def user(self):
        return UserFactory()

    @pytest.fixture
    def project(self):
        return ProjectFactory()

    @pytest.mark.django_db
    def test_get_project_success(self, api_client, user, project):
        api_client.force_authenticate(user=user)
        url = reverse("get-project", kwargs={"project_key": project.id})

        response = api_client.get(url)

        assert response.status_code == 200
        assert response.data["id"] == str(project.id)
        assert response.data["name"] == project.name
        assert response.data["description"] == project.description

    @pytest.mark.django_db
    def test_get_project_not_found(self, api_client, user):
        api_client.force_authenticate(user=user)
        url = reverse(
            "get-project",
            kwargs={"project_key": "00000000-0000-0000-0000-000000000000"},
        )

        response = api_client.get(url)

        assert response.status_code == 400
        assert "PROJECT_NOT_FOUND" in str(response.data)
