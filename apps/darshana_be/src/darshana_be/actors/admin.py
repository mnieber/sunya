from django.contrib import admin
from darshana_be.actors.models import Actor, Role


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("key",)
    search_fields = ("key",)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
