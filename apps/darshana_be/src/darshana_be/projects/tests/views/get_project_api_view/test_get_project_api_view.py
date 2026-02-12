import pytest
import deepdiff
from django.urls import reverse
from rest_framework.test import APIClient
from darshana_be.projects.tests.factories import ProjectFactory
from darshana_be.users.tests.factories import UserFactory
from darshana_be.scenarios.tests.factories import ScenarioFactory
from darshana_be.common.utils.test_utils import DeepDiffOperator, rhs_is_not_none


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
    def test_get_project_api_view_success(self, api_client, user):
        # Given
        api_client.force_authenticate(user=user)
        project = ProjectFactory(name="Test Project", description="Test Description")
        scenario = ScenarioFactory(name="Test Scenario", project=project)
        url = reverse("get-project", kwargs={"project_key": project.id})

        # When
        response = api_client.get(url)

        # Then
        assert response.status_code == 200

        result = response.json()
        expected = {
            "id": str(project.id),
            "name": "Test Project",
            "description": "Test Description",
            "scenarios": [
                {
                    "id": str(scenario.id),
                    "name": "Test Scenario",
                    "project": str(project.id),
                    "root_step": None,
                }
            ],
        }

        diff = deepdiff.DeepDiff(
            expected,
            result,
            custom_operators=[
                DeepDiffOperator(rhs_is_not_none, "id"),
                DeepDiffOperator(rhs_is_not_none, "scenarios.id"),
            ],
        )
        assert not diff, f"JSON response differs: {diff.pretty()}"

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
