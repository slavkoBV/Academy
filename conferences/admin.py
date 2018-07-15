from django.contrib import admin
from django.forms import ModelForm, ValidationError

from .models import Conference, ParticipantProfile, Thesis, Author, Participant


class AuthorInline(admin.StackedInline):
    model = Author
    extra = 0


class ThesisFormAdmin(ModelForm):

    def clean(self):
        authors = Author.objects.filter(thesis=self.instance.id)
        for a in authors:
            if a.participant.conference.id != self.cleaned_data['conference'].id:
                raise ValidationError('Автори повинні бути зареєстровані учасниками конференції на яку \
                                       подається доповідь')
        return self.cleaned_data


@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    list_display = ['title', 'section', 'conference', 'get_authors']
    list_filter = ['section']
    form = ThesisFormAdmin
    inlines = [AuthorInline]


@admin.register(ParticipantProfile)
class ParticipantProfileAdmin(admin.ModelAdmin):
    list_display = ['lastname', 'firstname', 'country', 'city', 'get_number_of_conferences']
    list_filter = ['degree', 'academic_status', 'country', 'city']
    readonly_fields = ['conferences']


class ParticipantInline(admin.StackedInline):
    model = Participant
    extra = 1


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ['title', 'level', 'date', 'status', 'get_number_of_participants']
    list_filter = ['status', 'date']
    inlines = [ParticipantInline]
