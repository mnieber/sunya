from django.db import models

from common.models import BaseModel


class Atlas(BaseModel):
    class Meta:
        verbose_name = "Atlas"
        verbose_name_plural = "Atlases"

    contents = models.JSONField()
    is_synced_with_jira = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Atlas of ${self.created_at}"
