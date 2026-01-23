from django.db import models

from common.models import BaseModel


class UserConsent(BaseModel):
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="consent",
    )
    accepted_terms = models.CharField(max_length=10, default="1.0.0")
    accepted_privacy_policy = models.CharField(max_length=10, default="")
    accepted_biometric_data_process = models.BooleanField(default=False)
