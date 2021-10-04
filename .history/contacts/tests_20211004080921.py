from django.test import Client, TestCase

from contacts.models import Contact

from .models import Contact

client = Client()


class ContactTest(TestCase):
    def setUp(self):
        Contact.objects.create(name="Henry", email="genryfordman")
        Contact.objects.create(name="Garry", email="genry@gmail.com")

    def test_contacts_model(self):
        contact_1st = Contact.objects.get(name="Henry")
        contact_2nd = Contact.objects.get(name="Garry")
        self.assertEqual(contact_1st, contact_1st.name)

    def test_contacts_available(self):
        response = client.get('http://localhost:8000/contacts')
        current = Contact.objects.all().count()
        self.assertEqual(response, )


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
