from django.contrib import admin

from atlases import models


@admin.register(models.Atlas)
class AtlasAdmin(admin.ModelAdmin):
    pass
