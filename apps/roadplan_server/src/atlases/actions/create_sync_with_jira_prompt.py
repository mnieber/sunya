from dataclassy import dataclass


@dataclass
class CreateSyncWithJiraPromptForm:
    snapshot: str


def create_sync_with_jira_prompt(
    create_sync_with_jira_prompt_form: CreateSyncWithJiraPromptForm,
):
    _validate_args(create_sync_with_jira_prompt_form)

    return ""


def _validate_args(create_sync_with_jira_prompt_form: CreateSyncWithJiraPromptForm):
    pass
