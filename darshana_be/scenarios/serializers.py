from rest_framework import serializers
from scenarios.models import Scenario
from scenarios.actions.create_scenario import CreateScenarioForm
from common.serializers import BaseModelSerializer, ReadSerializerMixin
from common.form_serializer import FormSerializer


class CreateScenarioFormSerializer(FormSerializer):
    class Meta:
        form_class = CreateScenarioForm


class ScenarioSerializer(ReadSerializerMixin, BaseModelSerializer):
    class Meta:
        model = Scenario
        fields = ['id', 'name', 'project', 'root_step']


class CreateScenarioRequestSerializer(FormSerializer):
    create_scenario_form = CreateScenarioFormSerializer()
