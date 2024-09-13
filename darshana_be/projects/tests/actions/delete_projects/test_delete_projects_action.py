import pytest
from projects.actions.delete_projects import delete_projects, DeleteProjectsForm
from projects.tests.factories import ProjectFactory
from projects.models import Project


class TestDeleteProjectsAction:
    @pytest.mark.django_db
    def test_delete_projects_action_success(self):
        # Given
        project1 = ProjectFactory()
        project2 = ProjectFactory()
        project3 = ProjectFactory()

        project_ids = [str(project1.id), str(project2.id)]

        # When
        deleted_count = delete_projects(DeleteProjectsForm(project_ids=project_ids))

        # Then
        assert deleted_count == 2
        assert not Project.objects.filter(id__in=[project1.id, project2.id]).exists()
        assert Project.objects.filter(id=project3.id).exists()

    @pytest.mark.django_db
    def test_delete_projects_action_with_nonexistent_ids(self):
        # Given
        project = ProjectFactory()
        nonexistent_id = "00000000-0000-0000-0000-000000000000"
        project_ids = [str(project.id), nonexistent_id]

        # When
        deleted_count = delete_projects(DeleteProjectsForm(project_ids=project_ids))

        # Then
        assert deleted_count == 1
        assert not Project.objects.filter(id=project.id).exists()
