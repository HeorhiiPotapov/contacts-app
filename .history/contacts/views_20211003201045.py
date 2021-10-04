from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import DeleteView

from .models import Contact


class ContactsListView(generic.ListView):
    model = Contact
    context_object_name = 'contacts'
    template_name = 'contacts/list.html'

    def get_queryset(self):
        contacts = Contact.objects.all()
        if self.kwargs.get('pk') is not None:
            contacts = contacts.filter(id=self.kwargs.get('pk'))
        return contacts


class ContactsCreateView(generic.CreateView):
    model = Contact
    template_name = "contacts/create.html"


class ContactsDestroyView(DeleteView):
    model = Contact
    success_url = 'contacts:list'
    template_name = "contacts/delete.html"
