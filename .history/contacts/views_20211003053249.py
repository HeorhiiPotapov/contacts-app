from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import DeleteView

from .models import Contact


class ContactsListView(generic.ListView):
    model = Contact
    context_object_name = 'contacts'
    template_name = 'contacts/list.html'


class ContactsCreateView(generic.CreateView):
    model = Contact
    template_name = "contacts/create.html"


class ContactsDeleteView(DeleteView):
    model = Contact
    template_name = "contacts/delete.html"
