from django.apps import AppConfig
from django.conf import settings
from roadplan.runtime.rules.load_config import load_config
from roadplan.runtime.utils.setup_logging import setup_logging
from roadplan.settings import (
    set_settings as set_roadplan_settings,
    Settings as RoadplanSettings,
)


class AppConfig(AppConfig):
    name = "app"

    def ready(self):
        load_config(settings.ROADPLAN_SETTINGS_FN)
        setup_logging(0, print)

        roadplan_settings = RoadplanSettings()
        roadplan_settings.jira_active_states = settings.JIRA_ACTIVE_STATES
        roadplan_settings.jira_issue_url_prefix = "https://landler.atlassian.net/"
        set_roadplan_settings(roadplan_settings)
