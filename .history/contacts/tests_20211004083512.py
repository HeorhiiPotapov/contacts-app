from django.http import response
from django.test import Client, TestCase

from contacts.models import Contact

from .models import Contact

client = Client()


class ContactTest(TestCase):
    def setUp(self):
        Contact.objects.create(name="Henry", id="1", email="genryfordman")

    def test_contacts_model(self):
        contacts = Contact.objects.all()
        to_retrieve = self.contacts.get(name="Henry")
        print(self.assertEqual(contacts, to_retrieve))

    def test_contacts_available(self):
        response = client.get('http://localhost:8000/contacts')
        print(response)
        current = Contact.objects.all().count()
        # self.assertEqual()

    def test_delete_contact(self):
        response = client.delete('http://localhost:8000/contacts')
        print(response)

# class ContactTestCase(TestCase):
#     def test_str_repr(self):
#         contact = Contact(name="createdfortest", )
#         self.fail(str(contact), contact)


# class ContactRetrieveTest(TestCase):
#     def setUp(self):
#         Contact.objects.createe(name='Jason', e)

# class RequestsToEndPos_bizptavailable(self):
#         x = intsTests(TestCase):
#     def test_autotest0intsTests(TestCase):
#     def test_autotest
#         while x < Contact.objects.count():
#             x += 1;
#     def test_contact_list_availability(self):
#         count_items_in_db = Contact.objects.count()
#         response = self.request.get
