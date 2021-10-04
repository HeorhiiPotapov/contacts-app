from rest_framework import generics
from ..models import Contact
from .serializers import ContactsSerializer


class MODELNAMEListAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactsSerializer

    def get_queryset(self):
        contacts = Contact.objects.all()
        if self.kwargs.get('pk') is not None:
            contact = contacts.filter(id=self.kwargs.get('pk'))
        return contacts
