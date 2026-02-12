import pytest
from darshana_be.projects.actions.import_scenario_spec import (
    import_scenario_spec,
    ImportScenarioSpecForm,
    NotExactlyOneRootNodeError,
)
from darshana_be.projects.tests.factories import ProjectFactory
from darshana_be.scenarios.models import Scenario
from darshana_be.steps.models import Step
from darshana_be.actors.models import Actor, Role


@pytest.mark.django_db
class TestImportScenarioSpecAction:
    @pytest.fixture
    def project(self):
        return ProjectFactory()

    @pytest.fixture
    def scenario_data(self):
        return {
            "type": "scenario",
            "order": 1,
            "scenario_name": "Test Scenario",
            "nodes": [
                {
                    "goal": "create a [Project] for the [alice@example.com+:user]",
                    "actors_introduced": [
                        {
                            "name": "my-test-project+:project",
                            "deltas": {
                                "name": "My Test Project",
                                "description": "A test project",
                            },
                        }
                    ],
                    "post_actor_key_by_role_name": {
                        "Project": "my-test-project+:project"
                    },
                    "child_nodes": [
                        {
                            "step": "The [alice@example.com+:user] visits the [projects+:route]"
                        },
                        {
                            "step": "The [alice@example.com+:user] submits the [project-form:component]"
                        },
                    ],
                }
            ],
        }

    def test_import_scenario_spec_success(self, project, scenario_data):
        # Given
        form = ImportScenarioSpecForm(scenario_data=scenario_data)

        # When
        scenario = import_scenario_spec(form, project)

        # Then
        assert isinstance(scenario, Scenario)
        assert scenario.name == "Test Scenario"
        assert scenario.project == project

        # Check root step
        root_step = scenario.root_step
        assert isinstance(root_step, Step)
        assert not root_step.parent_step
        assert root_step.fact[0].value == "create"
        assert root_step.fact[1].value == "a"
        assert root_step.fact[2].type_name == "role"
        assert root_step.fact[2].value == "Project"
        assert root_step.fact[3].value == "for"
        assert root_step.fact[4].value == "the"
        assert root_step.fact[5].type_name == "actor"
        assert root_step.fact[5].value == "alice@example.com+:user"

        # Check actors
        assert Actor.objects.filter(key="alice@example.com+:user").exists()
        assert Actor.objects.filter(key="my-test-project+:project").exists()

        # Check roles
        assert Role.objects.filter(name="Project").exists()

        # Check child steps
        child_steps = root_step.child_steps.all()
        assert len(child_steps) == 2
        assert child_steps[0].fact[1].value == "alice@example.com+:user"
        assert child_steps[0].fact[-1].value == "projects+:route"
        assert child_steps[1].fact[1].value == "alice@example.com+:user"
        assert child_steps[1].fact[-1].value == "project-form:component"

        # Check actor deltas
        assert "my-test-project+:project" in root_step.field_delta_set_by_actor_key
        assert root_step.field_delta_set_by_actor_key["my-test-project+:project"] == {
            "name": "My Test Project",
            "description": "A test project",
        }

    def test_import_scenario_spec_invalid_data(self, project):
        # Given
        invalid_data = {
            "scenario_name": "Invalid Scenario",
            "nodes": [],  # Empty nodes, which should not be valid
        }
        form = ImportScenarioSpecForm(scenario_data=invalid_data)

        # When/Then
        with pytest.raises(
            NotExactlyOneRootNodeError
        ):  # Assume it raises ValueError for invalid data
            import_scenario_spec(form, project)
