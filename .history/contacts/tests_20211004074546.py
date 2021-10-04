from django.test import TestCase, Client
from .models import Contact


client = Client()


class ContactTest(TestCase):
    def setUp(self):
        Contact.objects.create(name="Henry", email="genryfordman")

    def test_contacts_model(self):
        contact_1st = Contact.objects.get(name="Henry")
        contact_2nd = Contact.objects.get(name="Garry")
        self.assertEqual(contact_1st, contact_1st.name)


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
Garry
#     def test_contact_list_availability(self):
#         count_items_in_db = Contact.objects.count()
#         response = self.request.get
