from django.contrib import admin

from plot_questionnaires.models import PlotQuestionnaire


class PlotQuestionnaireInline(admin.StackedInline):
    model = PlotQuestionnaire
    extra = 0
    can_delete = False
    show_change_link = True
    readonly_fields = ["crc"]


@admin.register(PlotQuestionnaire)
class PlotQuestionnaireAdmin(admin.ModelAdmin):
    list_display = ["id", "crc", "created_at", "modified_at"]
    search_fields = ["id", "crc"]
    readonly_fields = ["crc"]
