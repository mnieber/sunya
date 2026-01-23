import pytest
from projects.actions.create_project import (
    CreateProjectForm,
    create_project,
    ProjectWithNameAlreadyExistsError,
)
from projects.tests.factories import ProjectFactory


class TestCreateProjectAction:
    @pytest.mark.django_db
    def test_create_project_action_success(self):
        # Given
        create_project_form = CreateProjectForm(
            name="Test Project", description="A test project"
        )

        # When
        project = create_project(create_project_form)

        # Then
        assert project.name == "Test Project"
        assert project.description == "A test project"

    @pytest.mark.django_db
    def test_create_project_action_with_existing_name(self):
        # Given
        ProjectFactory(name="Existing Project")

        create_project_form = CreateProjectForm(
            name="Existing Project", description="A test project"
        )

        # When / Then
        with pytest.raises(ProjectWithNameAlreadyExistsError):
            create_project(create_project_form)
