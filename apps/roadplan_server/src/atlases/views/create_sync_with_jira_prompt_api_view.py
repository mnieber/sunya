from common.permissions import user_is_authenticated
from atlases.serializers import CreateSyncWithJiraPromptFormSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import Serializer, CharField

from api.utils.extend_schema import extend_schema
from common.form_serializer import FormSerializer
from atlases.shortcuts import get_atlas_or_400
from atlases.actions.create_sync_with_jira_prompt import create_sync_with_jira_prompt


class CreateSyncWithJiraPromptRequestSerializer(FormSerializer):
    create_sync_with_jira_prompt_form = CreateSyncWithJiraPromptFormSerializer()


class SyncWithJiraPromptSerializer(Serializer):
    sync_with_jira_prompt_zip_fn = CharField()


class CreateSyncWithJiraPromptApiView(APIView):
    @extend_schema(
        request=CreateSyncWithJiraPromptRequestSerializer,
        responses={
            200: SyncWithJiraPromptSerializer,
        },
        data=dict(
            atlas=get_atlas_or_400,
        ),
        permissions=[(status.HTTP_401_UNAUTHORIZED, user_is_authenticated)],
    )
    def post(self, request, request_data, blog):
        try:
            sync_with_jira_prompt_zip_fn = create_sync_with_jira_prompt(
                create_sync_with_jira_prompt_form=request_data.create_sync_with_jira_prompt_form,
                blog=blog,
            )
        finally:
            pass

        return Response(
            SyncWithJiraPromptSerializer(sync_with_jira_prompt_zip_fn).data,
            status=status.HTTP_201_CREATED,
        )
