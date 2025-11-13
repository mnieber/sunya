
from atlases.models import Atlas
from dataclassy import dataclass


@dataclass
class UpdateAtlasForm:
    snapshot: str


def update_atlas(update_atlas_form: UpdateAtlasForm, atlas: Atlas):
    _validate_args(update_atlas_form, atlas)

    update_fields = []
    if update_atlas_form.snapshot is not None:
        atlas.snapshot = update_atlas_form.snapshot
        update_fields.append("snapshot")

    atlas.save(update_fields=update_fields)

    return atlas


def _validate_args(update_atlas_form: UpdateAtlasForm, atlas: Atlas):
    pass
