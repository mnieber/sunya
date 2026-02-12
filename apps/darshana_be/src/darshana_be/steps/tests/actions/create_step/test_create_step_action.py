import pytest
from darshana_be.steps.actions.create_step import CreateStepForm, create_step
from darshana_be.steps.models import Step, FactBit
from darshana_be.scenarios.tests.factories import ScenarioFactory
from darshana_be.steps.tests.factories import StepFactory
from darshana_be.steps.actions.create_step import AtLeastOneFactBitIsRequiredError


class TestCreateStepAction:
    @pytest.fixture
    def scenario(self):
        return ScenarioFactory()

    @pytest.mark.django_db
    def test_create_step_action_success(self, scenario):
        # Given
        create_step_form = CreateStepForm(
            fact=[
                FactBit(type_name="string", value="This is a test step"),
                FactBit(type_name="actor", value="test_actor"),
            ],
            field_delta_set_by_actor_key={
                "test_actor": {"field1": "value1", "field2": "value2"}
            },
        )

        # When
        step = create_step(create_step_form, scenario)

        # Then
        assert isinstance(step, Step)
        assert len(step.fact) == 2
        assert step.fact[0].type_name == "string"
        assert step.fact[0].value == "This is a test step"
        assert step.fact[1].type_name == "actor"
        assert step.fact[1].value == "test_actor"
        assert step.field_delta_set_by_actor_key == {
            "test_actor": {"field1": "value1", "field2": "value2"}
        }
        assert step.parent_step is None
        assert step.scenario == scenario

    @pytest.mark.django_db
    def test_create_step_action_with_parent(self, scenario):
        # Given
        parent_step = StepFactory(scenario=scenario)
        create_step_form = CreateStepForm(
            fact=[FactBit(type_name="string", value="Child step")],
            parent_step=parent_step,
        )

        # When
        step = create_step(create_step_form, scenario)

        # Then
        assert step.parent_step == parent_step

    @pytest.mark.django_db
    def test_create_step_action_no_facts(self, scenario):
        # Given
        create_step_form = CreateStepForm(fact=[])

        # When / Then
        with pytest.raises(AtLeastOneFactBitIsRequiredError):
            create_step(create_step_form, scenario)
