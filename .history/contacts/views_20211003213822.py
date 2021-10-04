from django.shortcuts import render
from django.urls import reverse_lazy
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
    success_url = 'reverse_lazy('contacts: list')'
    model = Contact
    template_name = "contacts/create.html"


class ContactsDestroyView(DeleteView):
    model = Contact
    success_url = reverse_lazy('contacts:list')
    template_name = "contacts/delete.html"
