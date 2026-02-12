from darshana_be.projects.actions.create_project import CreateProjectForm
from darshana_be.projects.actions.update_project import UpdateProjectForm
from darshana_be.projects.actions.import_scenario_spec import ImportScenarioSpecForm
from darshana_be.projects.actions.import_spec_files import ImportSpecFilesForm
from darshana_be.projects.models import Project
from darshana_be.common.form_serializer import FormSerializer
from darshana_be.common.serializers import BaseModelSerializer, ReadSerializerMixin
from darshana_be.projects.actions.delete_projects import DeleteProjectsForm
from darshana_be.scenarios.serializers import ScenarioSerializer


class CreateProjectFormSerializer(FormSerializer):
    class Meta:
        form_class = CreateProjectForm


class UpdateProjectFormSerializer(FormSerializer):
    class Meta:
        form_class = UpdateProjectForm


class ProjectSerializer(ReadSerializerMixin, BaseModelSerializer):
    scenarios = ScenarioSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["id", "name", "description", "scenarios"]


class ProjectLeadSerializer(ReadSerializerMixin, BaseModelSerializer):
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
