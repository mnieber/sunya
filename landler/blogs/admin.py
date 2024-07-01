from blogs import models
from django.contrib import admin


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass
