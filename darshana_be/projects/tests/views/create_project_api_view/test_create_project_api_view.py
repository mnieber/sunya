from api.utils.extend_schema.permissions import checks_permission
from common.permissions import user_is_authenticated
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from users.tests.factories import UserFactory
from projects.models import Project
from projects.views.create_project_api_view import CreateProjectApiView


class TestCreateProjectApiView:
    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def user(self):
        return UserFactory()

    @pytest.mark.django_db
    def test_create_project_api_view_success(self, api_client, user):
        # Given
        api_client.force_authenticate(user=user)
        url = reverse("create-project")
        project_data = {
            "create_project_form": {
                "name": "Test Project",
                "description": "This is a test project",
            }
        }

        # When
        response = api_client.post(url, data=project_data, format="json")

        # Then
        assert response.status_code == 201
        assert Project.objects.count() == 1
        project = Project.objects.first()
        assert project
        assert project.name == "Test Project"
        assert project.description == "This is a test project"
        assert response.data["id"] == str(project.id)
        assert response.data["name"] == project.name
        assert response.data["description"] == project.description

    @pytest.mark.django_db
    def test_create_project_api_view_unauthenticated(self):
        assert checks_permission(CreateProjectApiView.post, user_is_authenticated)
