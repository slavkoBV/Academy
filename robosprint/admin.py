from django.contrib import admin

from .models import RoboSprintInfo, Team, Participant, RoboSprintProject

MAX_OBJECTS = 1


@admin.register(RoboSprintInfo)
class InfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)


@admin.register(RoboSprintProject)
class ProjectAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)


class ParticipantInline(admin.StackedInline):
    model = Participant
    extra = 0


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['title', 'school', 'city', 'leader_fullname', 'approved']
    list_filter = ['city', 'approved']
    inlines = [ParticipantInline]


admin.site.register(Participant)
