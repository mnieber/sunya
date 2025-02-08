from django.db import models

from common.models import BaseModel


class BlockedToken(BaseModel):
    jti = models.TextField(unique=True)
