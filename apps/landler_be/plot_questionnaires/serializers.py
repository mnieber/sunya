from common.serializers import BaseModelSerializer, ReadSerializerMixin
from common.form_serializer import FormSerializer
from plot_questionnaires.models import PlotQuestionnaire
from plot_questionnaires.actions.create_plot_questionnaire import (
    CreatePlotQuestionnaireForm,
)


class CreatePlotQuestionnaireFormSerializer(FormSerializer):
    class Meta:
        form_class = CreatePlotQuestionnaireForm


class PlotQuestionnaireSerializer(ReadSerializerMixin, BaseModelSerializer):
    class Meta:
        model = PlotQuestionnaire
        fields = ["id", "values", "crc"]
