from django.test import TestCase
from .models import Contact


class ContactTestCase(TestCase):
    def test_str_repr(self):
        return self.fail('Contact test incomplete')
