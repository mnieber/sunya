from atlases.actions.create_atlas import create_atlas as create_atlas_model
from atlases.models import Atlas
from atlases.serializers import (
    AtlasBriefSerializer,
    AtlasSerializer,
    CreateAtlasFormSerializer,
)
from common.permissions import user_is_authenticated
from django.conf import settings
from roadplan.atlases.actions.create_atlas import create_atlas
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from roadplan.atlases.rules.create_atlas_snapshot import create_atlas_snapshot

from api.utils.extend_schema import extend_schema
from common.form_serializer import FormSerializer
from atlases.actions.create_atlas import CreateAtlasForm
from roadplan.error_reports.rules.create_error_report import create_error_report


class CreateAtlasRequestSerializer(FormSerializer):
    create_atlas_form = CreateAtlasFormSerializer()


class CreateAtlasApiView(APIView):
    @extend_schema(
        request=CreateAtlasRequestSerializer,
        responses={
            200: AtlasSerializer,
        },
        data=dict(),
        permissions=[(status.HTTP_401_UNAUTHORIZED, user_is_authenticated)],
    )
    def post(self, request, request_data):
        try:
            error_report = create_error_report()
            last_atlas = Atlas.objects.order_by("-created_at").first()
            atlas = create_atlas(
                error_report=error_report,
                historical_result_code_lut=(
                    last_atlas.snapshot.get("historical_result_code_lut", {})
                    if last_atlas
                    else {}
                ),
                roadmap_cache_by_roadmap_id=(
                    last_atlas.snapshot.get("roadmap_cache_by_roadmap_id", {})
                    if last_atlas
                    else {}
                ),
                notion_api_key=settings.NOTION_API_KEY,
                notion_roadmaps_page_id=settings.NOTION_ROADMAPS_PAGE_ID,
            )
            snapshot = create_atlas_snapshot(atlas)
            atlas_model = create_atlas_model(
                create_atlas_form=CreateAtlasForm(snapshot=snapshot)
            )
        finally:
            pass

        return Response(
            AtlasBriefSerializer(atlas_model).data, status=status.HTTP_201_CREATED
        )
