from rest_framework import serializers
from steps.models import Step
from common.serializers import BaseModelSerializer, ReadSerializerMixin
from common.form_serializer import FormSerializer
from dataclassy import asdict
from steps.actions.create_step import CreateStepForm


class FactBitSerializer(serializers.Serializer):
    type_name = serializers.ChoiceField(choices=["string", "role", "actor"])
    value = serializers.CharField()

    def to_representation(self, instance):
        return asdict(instance)


class StepSerializer(ReadSerializerMixin, BaseModelSerializer):
    fact = FactBitSerializer(many=True)

    class Meta:
        model = Step
        fields = ["id", "fact", "parent_step", "field_delta_set_by_actor_key"]


class CreateStepFormSerializer(FormSerializer):
    class Meta:
        form_class = CreateStepForm
