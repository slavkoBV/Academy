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


@admin.register(ParticipantProfile)
class ParticipantProfileAdmin(admin.ModelAdmin):
    list_display = ['lastname', 'firstname', 'country', 'city', 'get_number_of_conferences']
    list_filter = ['degree', 'academic_status', 'country', 'city']
    readonly_fields = ['conferences']


class ParticipantInline(admin.StackedInline):
    model = Participant
    extra = 1
    suit_classes = 'suit-tab suit-tab-participants'


class ThesisInline(admin.StackedInline):
    model = Thesis
    extra = 0
    verbose_name_plural = 'Доповіді'
    suit_classes = 'suit-tab suit-tab-thesises'


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'level', 'date_start', 'status', 'get_number_of_participants']
    list_filter = ['status', 'date_start']
    inlines = (ParticipantInline, ThesisInline)
    suit_form_tabs = (('general', 'Конференція'), ('participants', 'Учасники'), ('thesises', 'Доповіді'))
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['title', 'level', 'date_start', 'date_end', 'place', 'status', 'information_message']
         })
    ]


@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    list_display = ['title', 'section', 'conference', 'get_authors']
    list_filter = ['section', 'conference__title']
    form = ThesisFormAdmin
    inlines = [AuthorInline]

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('participant_profile', 'conference', 'section')
    list_filter = ('conference__title', 'section')
