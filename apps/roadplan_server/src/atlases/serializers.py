from atlases.actions.create_atlas import CreateAtlasForm
from atlases.models import Atlas
from atlases.actions.update_atlas import UpdateAtlasForm
from common.form_serializer import FormSerializer
from common.serializers import BaseModelSerializer, ReadSerializerMixin
from atlases.actions.delete_atlases import DeleteAtlasesForm
from common.form_serializer import FormSerializer


class CreateAtlasFormSerializer(FormSerializer):
    class Meta:
        form_class = CreateAtlasForm


class UpdateAtlasFormSerializer(FormSerializer):
    class Meta:
        form_class = UpdateAtlasForm


class AtlasSerializer(ReadSerializerMixin, BaseModelSerializer):
    class Meta:
        model = Atlas
        fields = ["id", "created_at", "contents"]


class AtlasBriefSerializer(ReadSerializerMixin, BaseModelSerializer):
    class Meta:
        model = Atlas
        fields = ["id", "created_at"]


class DeleteAtlasesFormSerializer(FormSerializer):
    class Meta:
        form_class = DeleteAtlasesForm
