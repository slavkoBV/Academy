from django.contrib import admin
from django import forms
from django.db import models
from django.forms import ModelForm, BaseInlineFormSet
from .models import Conference, UserProfile, Thesis, Author, Participant, Section, section_CHOICES


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['lastname', 'firstname', 'country', 'city', 'number_of_conferences']
    list_filter = ['lastname', 'degree', 'academic_status', 'country', 'city']
    search_fields = ['lastname']
    readonly_fields = ['conferences']

    def get_queryset(self, request):
        qs = super(UserProfileAdmin, self).get_queryset(request)
        qs = qs.annotate(models.Count('participant'))
        return qs

    def number_of_conferences(self, obj):
        return obj.participant__count

    number_of_conferences.admin_order_field = 'participant__count'
    number_of_conferences.short_description = 'Кількість конференцій'


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'order', 'title_eng', 'level', 'date_start', 'status', 'number_of_participants']
    list_filter = ['status', 'date_start']
    fieldsets = [
        (None, {
            'fields': ['title', 'order', 'title_eng', 'level', 'date_start', 'date_end', 'place', 'status',
                       'information_message', 'thesises_file']
        })
    ]

    def get_queryset(self, request):
        qs = super(ConferenceAdmin, self).get_queryset(request)
        qs = qs.annotate(models.Count('participant'))
        return qs

    def number_of_participants(self, obj):
        return obj.participant__count

    number_of_participants.admin_order_field = 'participant__count'
    number_of_participants.short_description = 'Кількість учасників'


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

conf_list = [(str(conf.id), str(conf.__str__())) for conf in Conference.objects.all()]


class ConferenceFilter(admin.SimpleListFilter):
    title = 'Конференція'
    parameter_name = 'conferences'

    def lookups(self, request, model_admin):

        return conf_list

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(conference__id=self.value())
        return queryset


class SectionFilter(admin.SimpleListFilter):
    title = 'Секція'
    parameter_name = 'sections'

    def lookups(self, request, model_admin):
        return section_CHOICES

    def queryset(self, request, queryset):
        if self.value():
            try:
                if isinstance(queryset[0], Thesis):
                    return queryset.filter(section=self.value())
                elif isinstance(queryset[0], Participant):
                    return queryset.filter(sections__title__contains=self.value())
            except IndexError:
                pass
        return queryset


@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    list_display = ['title', 'section', 'conference', 'get_authors']
    list_filter = [ConferenceFilter, SectionFilter]
    inlines = [AuthorInline]


class SectionInline(admin.StackedInline):
    model = Section
    extra = 0


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'conference', 'get_sections')
    list_max_show_all = 500
    list_filter = (ConferenceFilter, SectionFilter,)
    inlines = [SectionInline, ]
