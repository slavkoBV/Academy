from django.contrib import admin
from django import forms
from django.forms import ModelForm, ValidationError, BaseInlineFormSet
from .models import Conference, UserProfile, Thesis, Author, Participant, Section, section_CHOICES


class ThesisFormAdmin(ModelForm):
    def clean(self):
        authors = Author.objects.filter(thesis=self.instance.id)
        for a in authors:
            if a.participant.conference.id != self.cleaned_data['conference'].id:
                raise ValidationError('Автори повинні бути зареєстровані учасниками конференції на яку \
                                       подається доповідь')
            if self.cleaned_data['section'] not in a.participant.sections.values_list()[0][1]:
                raise ValidationError('Автори повинні бути зареєстровані в секції на яку \
                                       подається доповідь')
        return self.cleaned_data


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['lastname', 'firstname', 'country', 'city', 'get_number_of_conferences']
    list_filter = ['degree', 'academic_status', 'country', 'city']
    readonly_fields = ['conferences']


class ParticipantInline(admin.StackedInline):
    model = Participant
    extra = 0
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


class AuthorFormSet(BaseInlineFormSet):
    def _construct_form(self, i, **kwargs):
        kwargs['parent_object'] = self.instance
        return super()._construct_form(i, **kwargs)

    @property
    def empty_form(self):
        form = self.form(
            auto_id=self.auto_id,
            prefix=self.add_prefix('__prefix__'),
            empty_permitted=True,
            parent_object=self.instance,
        )
        self.add_fields(form, None)
        return form


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
        name = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        self.parent_object = kwargs.pop('parent_object', None)
        super().__init__(*args, **kwargs)
        thesis = None
        if self.parent_object.id:
            thesis = Thesis.objects.get(id=self.parent_object.id)
        if thesis:
            self.fields['participant'].queryset = Participant.objects.filter(conference=thesis.conference)
        else:
            self.fields['participant'].queryset = Participant.objects.none()


class AuthorInline(admin.StackedInline):
    model = Author
    extra = 0
    verbose_name_plural = 'Автори'
    formset = AuthorFormSet
    form = AuthorForm


@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    list_display = ['title', 'section', 'conference', 'get_authors']
    list_filter = ['conference__title', 'section']
    form = ThesisFormAdmin
    inlines = [AuthorInline]


class SectionInline(admin.StackedInline):
    model = Section
    extra = 0


class ParticipantFilter(admin.SimpleListFilter):
    title = 'Секція'
    parameter_name = 'sections'

    def lookups(self, request, model_admin):
        return section_CHOICES

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(sections__title__contains=self.value())
        return queryset


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'conference', 'get_sections')
    list_filter = ('conference__title', ParticipantFilter)
    inlines = [SectionInline, ]
