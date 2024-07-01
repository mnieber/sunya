import typing as T

import django.contrib.auth.models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel
from users.actions.create_superuser import create_superuser
from users.actions.delete_user import delete_user


class UserManager(django.contrib.auth.models.UserManager):
    def create_superuser(
        self, username=None, email=None, password=None, **extra_fields
    ):
        return create_superuser(email, password, **extra_fields)

    def active_with_confirmed_email(self):
        return self.filter(email_activated=True, is_active=True)


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS: T.List[str] = []

    email = models.EmailField(
        max_length=settings.MAX_EMAIL_LENGTH,
        unique=True,
        error_messages={"unique": _("User with this email already exists.")},
    )
    is_email_activated = models.BooleanField(default=False)
    firstname = models.CharField(max_length=255, default="anonymous")
    lastname = models.CharField(max_length=255, default="anonymous")
    is_active = models.BooleanField("active", default=False)
    is_anonymous = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField("date joined", auto_now_add=True)
    language = models.CharField(
        max_length=10,
        choices=settings.LANGUAGES,
        default="unknown",
    )

    @property
    def fullname(self):
        return self.firstname + " " + self.lastname

    def _delete(self, using=None):
        super().delete(using=using)

    def delete(self, using=None):
        delete_user(self, using=using)
