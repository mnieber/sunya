import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from projects.tests.factories import ProjectFactory
from users.tests.factories import UserFactory


class TestUpdateProjectApiView:
    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def user(self):
        return UserFactory()

    @pytest.mark.django_db
    def test_update_project_api_view_success(self, api_client, user):
        # Given
        api_client.force_authenticate(user=user)
        project = ProjectFactory(name="Old Name", description="Old description")
        url = reverse("update-project", kwargs={"project_key": str(project.id)})
        project_data = {
            "update_project_form": {
                "name": "New Name",
                "description": "New description",
            }
        }

        # When
        response = api_client.post(url, data=project_data, format="json")

        # Then
        assert response.status_code == 200
        project.refresh_from_db()
        assert project.name == "New Name"
        assert project.description == "New description"
        assert response.data["id"] == str(project.id)
        assert response.data["name"] == project.name
        assert response.data["description"] == project.description

    @pytest.mark.django_db
    def test_update_project_api_view_nonexistent_project(self, api_client, user):
        # Given
        api_client.force_authenticate(user=user)
        url = reverse(
            "update-project",
            kwargs={"project_key": "00000000-0000-0000-0000-000000000000"},
        )
        project_data = {
            "update_project_form": {
                "name": "New Name",
                "description": "This should fail",
            }
        }

        # When
        response = api_client.post(url, data=project_data, format="json")

        # Then
        assert response.status_code == 400

        errors = response.data.get("errors", [])
        assert len(errors) == 1 and errors[0]["code"] == "PROJECT_NOT_FOUND"
