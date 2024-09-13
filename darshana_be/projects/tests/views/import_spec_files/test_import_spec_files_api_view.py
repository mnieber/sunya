import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from projects.tests.factories import ProjectFactory
from users.tests.factories import UserFactory
from django.core.files.uploadedfile import SimpleUploadedFile


class TestImportSpecFilesApiView:
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
    def test_import_spec_files_success(self, api_client, user, project):
        api_client.force_authenticate(user=user)
        url = reverse("import-spec-files", kwargs={"project_key": project.id})

        scenario_content = b"""
scenario_name: test-scenario
nodes:
  - goal: root
    child_nodes:
      - goal: test goal
        """
        scenario_file = SimpleUploadedFile(
            "test_scenario.yaml", scenario_content, content_type="application/x-yaml"
        )

        module_content = b"""
name: test_module
models:
  - name: TestModel
    fields:
      - name: id
        type: UUID
        """
        module_file = SimpleUploadedFile(
            "test_module.yaml", module_content, content_type="application/x-yaml"
        )

        response = api_client.post(
            url,
            {"files": [scenario_file, module_file]},
            format="multipart",
        )

        assert response.status_code == 200
        assert "id" in response.data
        assert response.data["name"] == project.name

    @pytest.mark.django_db
    def test_import_spec_files_invalid_file(self, api_client, user, project):
        api_client.force_authenticate(user=user)
        url = reverse("import-spec-files", kwargs={"project_key": project.id})

        invalid_file = SimpleUploadedFile(
            "invalid.yaml", b"""invalid content""", content_type="application/x-yaml"
        )

        response = api_client.post(
            url,
            {"files": [invalid_file]},
            format="multipart",
        )

        assert response.status_code == 400
        assert "errors" in response.data
