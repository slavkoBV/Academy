from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')
    date_hierarchy = 'date_created'
    prepopulated_fields = {'annotation': ('title',)}
