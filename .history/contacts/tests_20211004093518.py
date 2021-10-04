from django.http import response
from django.test import Client, TestCase
from django.urls import reverse
import json
from rest_framework import status
from contacts.api.views import ContactsSerializer
from contacts.models import Contact
from .models import Contact
from .api.serializers import ContactsSerializer

client = Client()


class GetAllContactsTest(TestCase):
    """ Test module for GET all contacts API """

    def setUp(self):
        Contact.objects.create(

            name='Contact', email='contact@contact.com')
        Contact.objects.create(

            name='Contact 2', email='contact2@contact.com')
        Contact.objects.create(

            name='Contact 3', email='contact3@contact.com')
        Contact.objects.create(

            name='Contact 4', email='contact4@contact.com')

    def test_get_all_contacts(self):
        response = client.get(reverse('get_post_contacts'))
        contacts = Contact.objects.all()
        serializer = ContactsSerializer(contacts, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleContactTest(TestCase):

    def setUp(self):
        self.contact = Contact.objects.create(
            name='contact', email='contact@contact.com')
        self.contact2 = Contact.objects.create(
            name='contact2', email='contact2@contact.com')
        self.contact3 = Contact.objects.create(
            name='contact3', email='contact3@contact.com')
        self.contact4 = Contact.objects.create(
            name='contact4', email='contact4@contact.com')

    def test_get_valid_single_contact(self):
        response = client.get(
            reverse('get_delete_update_contact', kwargs={'pk': self.contact.pk}))
        contact = Contact.objects.get(pk=self.contact2.pk)
        serializer = ContactsSerializer(contact)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_contact(self):
        response = client.get(
            reverse('get_delete_update_contact', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewContactTest(TestCase):
    """ Test module for inserting a new contact """

    def setUp(self):
        self.valid_payload = {
            'name': 'Contact ',
            'email': 'contact@contact.com',
        }
        self.invalid_payload = {
            'name': '',
            'email': 'contact2@contact.com',
        }

    def test_create_valid_contact(self):
        response = client.post(
            reverse('contacts:create'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_contact(self):
        response = client.post(
            reverse('contacts:create'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleContactTest(TestCase):
    """ Test module for deleting an existing experiment record """

    def setUp(self):
        self.project = Contact.objects.create(
            name='Project', email='project@project.com')
        self.project2 = Contact.objects.create(
            name='Project 2', email='project2@project.com')

    def test_valid_delete_contact(self):
        response = client.delete(
            reverse('get_delete_update_', kwargs={'pk': self.project2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_contact(self):
        response = client.delete(
            reverse('get_delete_update_experiment', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
