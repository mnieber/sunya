from common.permissions import user_is_authenticated
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from projects.tests.factories import ProjectFactory
from users.tests.factories import UserFactory
from api.utils.extend_schema.permissions import checks_permission
from projects.views.delete_projects_api_view import DeleteProjectsApiView


class TestDeleteProjectsApiView:
    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def user(self):
        return UserFactory()

    @pytest.mark.django_db
    def test_delete_projects_api_view_success(self, api_client, user):
        # Given
        api_client.force_authenticate(user=user)
        project1 = ProjectFactory()
        project2 = ProjectFactory()
        project3 = ProjectFactory()
        url = reverse("delete-projects")

        # When
        response = api_client.post(
            url,
            data={"project_ids": [str(project1.id), str(project2.id)]},
            format="json",
        )

        # Then
        assert response.status_code == 200
        assert response.data["deleted_count"] == 2
        assert not ProjectFactory._meta.model.objects.filter(
            id__in=[project1.id, project2.id]
        ).exists()
        assert ProjectFactory._meta.model.objects.filter(id=project3.id).exists()

    @pytest.mark.django_db
    def test_delete_projects_api_view_unauthenticated(self):
        assert checks_permission(DeleteProjectsApiView.post, user_is_authenticated)
