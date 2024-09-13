from projects.actions.create_project import CreateProjectForm
from projects.actions.save_project import SaveProjectForm
from projects.actions.import_scenario_spec import ImportScenarioSpecForm
from projects.actions.import_spec_files import ImportSpecFilesForm
from projects.models import Project
from common.form_serializer import FormSerializer
from common.serializers import BaseModelSerializer, ReadSerializerMixin
from projects.actions.delete_projects import DeleteProjectsForm


class CreateProjectFormSerializer(FormSerializer):
    class Meta:
        form_class = CreateProjectForm


class SaveProjectFormSerializer(FormSerializer):
    class Meta:
        form_class = SaveProjectForm


class ProjectSerializer(ReadSerializerMixin, BaseModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "description"]


class ImportScenarioSpecFormSerializer(FormSerializer):
    class Meta:
        form_class = ImportScenarioSpecForm


class ImportSpecFilesFormSerializer(FormSerializer):
    class Meta:
        form_class = ImportSpecFilesForm


class DeleteProjectsFormSerializer(FormSerializer):
    class Meta:
        form_class = DeleteProjectsForm
