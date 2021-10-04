from django.test import TestCase
from .models import Contact


class ContactTestCase(TestCase):
    def test_str_repr(self):
        contact = Contact(name="createdfortest", email="test@gmail.com")
        self.fail(str(contact), contact)


# class RequestsToEndPointsTests(TestCase):
#     def test_autotests_bizptavailable(self):
#         x = 0
#         while x < Contact.objects.count():
#             x += 1;

#     def test_contact_list_availability(self):
#         count_items_in_db = Contact.objects.count()
#         response = self.request.get
