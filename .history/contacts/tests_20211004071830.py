from django.test import TestCase, Client
from .models import Contact


client = Client()


class ContactTest(TestCase):
    pas

# class ContactTestCase(TestCase):
#     def test_str_repr(self):
#         contact = Contact(name="createdfortest", )
#         self.fail(str(contact), contact)


# class ContactRetrieveTest(TestCase):
#     def setUp(self):
#         Contact.objects.createe(name='Jason', e)

    # class RequestsToEndPointsTests(TestCase):
    #     def test_autotests_bizptavailable(self):
    #         x = 0
    #         while x < Contact.objects.count():
    #             x += 1;

    #     def test_contact_list_availability(self):
    #         count_items_in_db = Contact.objects.count()
    #         response = self.request.get
