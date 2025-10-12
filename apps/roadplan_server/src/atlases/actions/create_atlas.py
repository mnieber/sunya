
from atlases.models import Atlas
from dataclassy import dataclass
from django.contrib.auth import get_user_model

User = get_user_model()


@dataclass
class CreateAtlasForm:
    contents: str


def create_atlas(create_atlas_form: CreateAtlasForm):
    _validate_args(create_atlas_form)

    atlas = Atlas(contents=create_atlas_form.contents)
    atlas.save()

    return atlas


def _validate_args(create_atlas_form: CreateAtlasForm):
    pass
