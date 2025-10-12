from atlases.models import Atlas
from rest_framework.exceptions import ValidationError
from common.utils.ids import is_uuid


def get_atlas_or_400(atlas_key):
    kwargs = {"pk" if is_uuid(atlas_key) else "slug": atlas_key}

    atlas = Atlas.objects.filter(**kwargs).first()
    if not atlas:
        raise ValidationError(code="ATLAS_NOT_FOUND")

    return atlas
