from django.test import TestCase
from .models import Contact


class ContactTestCase(TestCase):
    def test_str_repr(self):
        contact = Contact(name="createdfortest", email="test@gmail.com")
        self.fail(str(contact), contact.name)
