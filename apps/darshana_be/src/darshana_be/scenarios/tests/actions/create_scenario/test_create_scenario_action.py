import pytest
from darshana_be.scenarios.actions.create_scenario import (
    ScenarioWithNameAlreadyExistsError,
    CreateScenarioForm,
    create_scenario,
)
from darshana_be.scenarios.tests.factories import ScenarioFactory
from darshana_be.projects.tests.factories import ProjectFactory


class TestCreateScenarioAction:
    @pytest.fixture()
    def project(self):
        return ProjectFactory()

    @pytest.mark.django_db
    def test_create_scenario_action_success(self, project):
        # Given
        create_scenario_form = CreateScenarioForm(name="Test Scenario", order=1)

        # When
        scenario = create_scenario(create_scenario_form, project=project)

        # Then
        assert scenario.name == "Test Scenario"
        assert scenario.project == project

    @pytest.mark.django_db
    def test_create_scenario_action_with_existing_name(self, project):
        # Given
        ScenarioFactory(name="Existing Scenario", project=project)

        create_scenario_form = CreateScenarioForm(name="Existing Scenario", order=1)

        # When / Then
        with pytest.raises(ScenarioWithNameAlreadyExistsError):
            create_scenario(create_scenario_form, project=project)
