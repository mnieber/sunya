from django.contrib import admin

from organizations.models import Organization, OrganizationMembership


class OrganizationMembershipInline(admin.TabularInline):
    model = OrganizationMembership
    extra = 1
    raw_id_fields = ("user",)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    inlines = [OrganizationMembershipInline]


@admin.register(OrganizationMembership)
class OrganizationMembershipAdmin(admin.ModelAdmin):
    list_display = ["organization", "user", "role"]
    list_filter = ["role"]
    search_fields = ["organization__name", "user__email"]
    raw_id_fields = ("user", "organization")
