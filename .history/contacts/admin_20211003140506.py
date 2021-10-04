from django.contrib import admin
from .models import Contact


@sdmin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
