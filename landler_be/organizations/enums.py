from django.db import models


class UserInOrganizationRoles(models.TextChoices):
    ADMIN = "admin", "Admin"
    EDITOR = "editor", "Editor"
