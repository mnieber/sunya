from django.contrib import admin
from steps.models import Step


class StepInline(admin.TabularInline):
    model = Step
    fk_name = 'parent_step'
    extra = 1


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ('id', 'scenario', 'parent_step')
    list_filter = ('scenario',)
    search_fields = ('id', 'scenario__name')
    inlines = (StepInline,)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('scenario', 'parent_step')
