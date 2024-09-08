import pytest
from projects.actions.save_project import (
    SaveProjectForm,
    save_project,
    ProjectWithNameAlreadyExistsError,
)
from projects.tests.factories import ProjectFactory


class TestSaveProjectAction:
    @pytest.mark.django_db
    def test_save_project_action_success(self):
        # Given
        project = ProjectFactory(name="Old Name", description="Old description")
        save_project_form = SaveProjectForm(
            name="New Name", description="New description"
        )

        # When
        updated_project = save_project(save_project_form, project)

        # Then
        assert updated_project.name == "New Name"
        assert updated_project.description == "New description"

    @pytest.mark.django_db
    def test_save_project_action_with_existing_name(self):
        # Given
        ProjectFactory(name="Existing Project")
        project = ProjectFactory(name="Project to Update")

        save_project_form = SaveProjectForm(
            name="Existing Project", description="Updated description"
        )

        # When / Then
        with pytest.raises(ProjectWithNameAlreadyExistsError):
            save_project(save_project_form, project)
