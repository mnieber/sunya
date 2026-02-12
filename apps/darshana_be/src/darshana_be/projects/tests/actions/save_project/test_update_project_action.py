import pytest
from darshana_be.projects.actions.update_project import (
    UpdateProjectForm,
    update_project,
    ProjectWithNameAlreadyExistsError,
)
from darshana_be.projects.tests.factories import ProjectFactory


class TestUpdateProjectAction:
    @pytest.mark.django_db
    def test_update_project_action_success(self):
        # Given
        project = ProjectFactory(name="Old Name", description="Old description")
        update_project_form = UpdateProjectForm(
            name="New Name", description="New description"
        )

        # When
        updated_project = update_project(update_project_form, project)

        # Then
        assert updated_project.name == "New Name"
        assert updated_project.description == "New description"

    @pytest.mark.django_db
    def test_update_project_action_with_existing_name(self):
        # Given
        ProjectFactory(name="Existing Project")
        project = ProjectFactory(name="Project to Update")

        update_project_form = UpdateProjectForm(
            name="Existing Project", description="Updated description"
        )

        # When / Then
        with pytest.raises(ProjectWithNameAlreadyExistsError):
            update_project(update_project_form, project)
