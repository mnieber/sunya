from atlases.models import Atlas
from dataclassy import dataclass


@dataclass
class CreateSyncWithJiraPromptForm:
    contents: str


def create_sync_with_jira_prompt(
    create_sync_with_jira_prompt_form: CreateSyncWithJiraPromptForm,
):
    _validate_args(create_sync_with_jira_prompt_form)

    atlas = Atlas(contents=create_sync_with_jira_prompt_form.contents)
    atlas.save()

    return atlas


def _validate_args(create_sync_with_jira_prompt_form: CreateSyncWithJiraPromptForm):
    pass
