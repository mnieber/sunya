from darshana_be.common.permissions import user_is_authenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from darshana_be.projects.models import Project
from darshana_be.projects.serializers import ProjectLeadSerializer
from darshana_be.api.utils.extend_schema import extend_schema


class ProjectLeadsPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 100


class GetProjectLeadsApiView(APIView):
    pagination_class = ProjectLeadsPagination

    @extend_schema(
        parameters=[
            {
                "name": "page",
                "in": "query",
                "description": "Page number",
                "required": False,
                "type": "integer",
            },
            {
                "name": "page_size",
                "in": "query",
                "description": "Number of items per page",
                "required": False,
                "type": "integer",
            },
        ],
        responses={
            200: ProjectLeadSerializer(many=True),
        },
        permissions=[(status.HTTP_401_UNAUTHORIZED, user_is_authenticated)],
    )
    def get(self, request):
        projects = Project.objects.all().order_by("name")
        paginator = self.pagination_class()
        paginated_projects = paginator.paginate_queryset(projects, request)
        serializer = ProjectLeadSerializer(paginated_projects, many=True)
        return paginator.get_paginated_response(serializer.data)
