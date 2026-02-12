from django.contrib import admin
from darshana_be.scenarios.models import Scenario


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'root_step')
    search_fields = ('name', 'project__name')
    list_filter = ('project',)
