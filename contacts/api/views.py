from rest_framework import generics
from ..models import Contact
from .serializers import ContactsSerializer, ContactsCreateSerializer


class ContactsListAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactsSerializer

    def get_queryset(self):
        contacts = Contact.objects.all()
        if self.kwargs.get('pk') is not None:
            contact = contacts.filter(id=self.kwargs.get('pk'))
        return contacts


class ContactsDestroyAPIView(generics.DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactsSerializer
    lookup_field = 'pk'


class ContactsCreateAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactsCreateSerializer
