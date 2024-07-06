from django.contrib.auth import get_user_model
from django.db import models

from common.fields import SingleLineTextField
from common.models import BaseModel
from organizations.enums import UserInOrganizationRoles

User = get_user_model()


class Organization(BaseModel):
    name = SingleLineTextField()

    def __str__(self):
        return self.name


class OrganizationMembership(BaseModel):
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="memberships"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="organization_memberships"
    )
    role = models.CharField(max_length=20, choices=UserInOrganizationRoles.choices)

    class Meta:
        unique_together = ("organization", "user", "role")

    def __str__(self):
        return f"{self.user.email} - {self.organization.name} ({self.role})"
