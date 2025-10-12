import typing as T

from atlases.models import Atlas
from dataclassy import dataclass


@dataclass
class UpdateAtlasForm:
    contents: str


def update_atlas(update_atlas_form: UpdateAtlasForm, atlas: Atlas):
    _validate_args(update_atlas_form, atlas)

    update_fields = []
    if update_atlas_form.contents is not None:
        atlas.contents = update_atlas_form.contents
        update_fields.append("contents")

    atlas.save(update_fields=update_fields)

    return atlas


def _validate_args(update_atlas_form: UpdateAtlasForm, atlas: Atlas):
    pass
