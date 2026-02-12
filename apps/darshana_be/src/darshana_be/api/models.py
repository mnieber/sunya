from django.db import models

from darshana_be.common.models import BaseModel


class BlockedToken(BaseModel):
    jti = models.TextField(unique=True)
