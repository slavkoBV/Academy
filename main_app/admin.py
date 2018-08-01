from django.contrib import admin
from .models import Contact, PhoneNumber, Email


class PhoneInline(admin.StackedInline):
    model = PhoneNumber
    extra = 0
    suit_classes = 'suit-tab suit-tab-phone'

class EmailInline(admin.StackedInline):
    model = Email
    extra = 0
    suit_classes = 'suit-tab suit-tab-emails'

@admin.register(Contact)
class ContanctAdmin(admin.ModelAdmin):
    inlines = (PhoneInline, EmailInline)
    suit_form_tabs = (('general', 'Адреса'), ('phone', 'Телефони'), ('emails', 'E-mails'))
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['address']
        })
    ]
