from atlases.models import Atlas
from django_filters import rest_framework as filters


class AtlasFilterSet(filters.FilterSet):
    sort = filters.OrderingFilter(fields=["created_at"])

    class Meta:
        model = Atlas
        fields = {"created_at": ["exact"]}
