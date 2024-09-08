from django.contrib import admin
from projects.models import Project
from scenarios.models import Scenario


class ScenarioInline(admin.TabularInline):
    model = Scenario
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    inlines = [ScenarioInline]
