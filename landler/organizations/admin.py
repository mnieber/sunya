from django.contrib import admin
from organizations import models


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass
