from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.utils.extend_schema import extend_schema
from organizations.permissions import user_is_organization_member
from organizations.serializers import OrganizationSerializer
from organizations.shortcuts import get_organization_or_404
from common.serializers import EmptySerializer


class SetActiveOrganizationApiView(APIView):
    @extend_schema(
        request=EmptySerializer,
        responses={
            200: OrganizationSerializer,
        },
        data=dict(
            organization=get_organization_or_404,
        ),
        permissions=[
            (
                403,
                user_is_organization_member,
                "User must be a member of the organization.",
            ),
        ],
    )
    def post(self, request, organization):
        request.session["active_organization_id"] = str(organization.id)
        request.session.modified = True
        return Response(
            OrganizationSerializer(organization).data, status=status.HTTP_200_OK
        )
