from django.shortcuts import render
from django.views import generic
from .models import Contact


class ContactsListView(generic.ListView):
    model = Contact
    context_object_name = 'contacts'
    template_name = 'contacts/list.html'
