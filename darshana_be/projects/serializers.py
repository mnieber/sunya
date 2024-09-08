from projects.actions.create_project import CreateProjectForm
from projects.actions.save_project import SaveProjectForm
from projects.models import Project
from common.form_serializer import FormSerializer
from common.serializers import BaseModelSerializer, ReadSerializerMixin


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


class DeleteProjectsFormSerializer(FormSerializer):
    class Meta:
        form = list[str]  # This represents the list of project IDs to delete
