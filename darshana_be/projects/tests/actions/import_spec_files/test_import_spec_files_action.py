import pytest
from unittest.mock import patch
from django.core.files.uploadedfile import SimpleUploadedFile
from projects.actions.import_spec_files import import_spec_files, ImportSpecFilesForm
from projects.tests.factories import ProjectFactory
from scenarios.models import Scenario


@pytest.mark.django_db
class TestImportSpecFilesAction:
    @pytest.fixture
    def project(self):
        return ProjectFactory()

    @pytest.fixture
    def scenario_spec_file(self):
        content = """
        scenario_name: Test Scenario
        nodes:
          - goal: "create a [Project] for the [alice@example.com+:user]"
            child_nodes:
              - step: "The [alice@example.com+:user] visits the [projects+:route]"
        """
        return SimpleUploadedFile("scenario.yaml", content.encode("utf-8"))

    @pytest.fixture
    def module_spec_file(self):
        content = """
        name: test_module
        models:
          - name: TestModel
            fields:
              - name: id
                type: UUID
              - name: name
                type: str
        """
        return SimpleUploadedFile("module.yaml", content.encode("utf-8"))

    @patch("projects.actions.import_spec_files.import_scenario_spec")
    def test_import_spec_files_success(
        self, mock_import_scenario_spec, project, scenario_spec_file, module_spec_file
    ):
        # Given
        form = ImportSpecFilesForm(files=[scenario_spec_file, module_spec_file])

        # When
        import_spec_files(form, project)

        # Then
        # Check that import_scenario_spec was called once
        mock_import_scenario_spec.assert_called_once()
        args, kwargs = mock_import_scenario_spec.call_args
        assert args[1] == project
        assert args[0].scenario_data["scenario_name"] == "Test Scenario"

    def test_import_spec_files_deletes_existing_data(self, project, scenario_spec_file):
        # Given
        existing_scenario = Scenario.objects.create(
            name="Existing Scenario", project=project
        )
        form = ImportSpecFilesForm(files=[scenario_spec_file])

        # When
        with patch("projects.actions.import_spec_files.import_scenario_spec"):
            import_spec_files(form, project)

        # Then
        assert not Scenario.objects.filter(id=existing_scenario.id).exists()
