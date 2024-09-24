from django.db import models


class ChecklistItemNames(models.TextChoices):
    WELCOME = "Welcome"
    JOIN_DEMO_ORG = "Join the demo org"
    ADD_ORGANIZATION = "Add your organization"
    CREATE_PROJECT = "Create a project"
    ADD_PLOT = "Add a plot"
    TRIGGER_ANALYSIS = "Trigger a project analysis"
