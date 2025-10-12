from dataclassy import dataclass
from typing import List
from django.db import transaction
from atlases.models import Atlas


@dataclass
class DeleteAtlasesForm:
    atlas_ids: List[str]


@transaction.atomic
def delete_atlases(delete_atlases_form: DeleteAtlasesForm, atlas: Atlas):
    atlases = Atlas.objects.filter(id__in=delete_atlases_form.atlas_ids, atlas=atlas)

    if len(atlases) != len(delete_atlases_form.atlas_ids):
        found_ids = set(str(post.id) for post in atlases)
        missing_ids = set(delete_atlases_form.atlas_ids) - found_ids
        raise AtlasesNotFoundError(missing_ids)

    deleted_count = atlases.delete()[0]
    return deleted_count


class AtlasesNotFoundError(Exception):
    def __init__(self, missing_ids):
        self.missing_ids = missing_ids
        super().__init__(f"Atlases not found: {missing_ids}")
