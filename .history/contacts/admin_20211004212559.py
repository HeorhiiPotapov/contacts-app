from django.contrib import admin
from .models import ContactModel


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name',)


admin.site.register(ContactModel, ContactAdmin)
