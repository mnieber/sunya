from atlases.models import Atlas
from dataclassy import dataclass
from django.contrib.auth import get_user_model

User = get_user_model()


@dataclass
class CreateAtlasForm:
    snapshot: str


def create_atlas(create_atlas_form: CreateAtlasForm):
    _validate_args(create_atlas_form)

    atlas = Atlas(
        snapshot=create_atlas_form.snapshot,
        is_synced_with_jira=False,
    )
    atlas.save()

    return atlas


def _validate_args(create_atlas_form: CreateAtlasForm):
    pass
