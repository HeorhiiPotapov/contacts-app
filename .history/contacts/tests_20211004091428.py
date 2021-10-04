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

            name='Project', email='project@project.com')
        Contact.objects.create(

            name='Project 2', email='project2@project.com')
        Contact.objects.create(

            name='Project 3', email='project3@project.com')
        Contact.objects.create(

            name='Project 4', email='project4@project.com')

    def test_get_all_contacts(self):
        response = client.get(reverse('get_post_contacts'))
        contacts = Contact.objects.all()
        serializer = ContactsSerializer(contacts, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleContactTest(TestCase):

    def setUp(self):
        self.contact = Contact.objects.create(
            name='contact', email='project@project.com')
        self.contact = Contact.objects.create(
            name='contact2', email='project2@project.com')
        self.project3 = Contact.objects.create(
            name='contact3', email='project3@project.com')
        self.project4 = Contact.objects.create(
            name='contact4', email='project4@project.com')

    def test_get_valid_single_contact(self):
        response = client.get(
            reverse('get_delete_update_contact', kwargs={'pk': self.project2.pk}))
        contact = Contact.objects.get(pk=self.project2.pk)
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
            'name': 'Project',
            'email': 'project@project.com',
            'score': 1,

        }
        self.invalid_payload = {
            'name': '',
            'email': 'project2@project.com',
            'score': 2,
        }

    def test_create_valid_experiment(self):
        response = client.post(
            reverse('get_post_contacts'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_experiment(self):
        response = client.post(
            reverse('get_post_contacts'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleExperimentTest(TestCase):
    """ Test module for updating an existing experiment record """

    def setUp(self):
        self.project = Experiment.objects.create(
            name='Project', email='project@project.com')
        self.project2 = Experiment.objects.create(
            name='Project 2', email='project2@project.com')
        self.valid_payload = {
            'name': 'Project',
            'email': 'project3@project.com',
            'score': 6
        }
        self.invalid_payload = {
            'name': '',
            'email': 'project5@project.com',
            'score': 5
        }

    def test_valid_update_experiment(self):
        response = client.put(
            reverse('get_delete_update_experiment',
                    kwargs={'pk': self.project2.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_experiment(self):
        response = client.put(
            reverse('get_delete_update_experiment',
                    kwargs={'pk': self.project2.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleExperimentTest(TestCase):
    """ Test module for deleting an existing experiment record """

    def setUp(self):
        self.project = Experiment.objects.create(
            name='Project', email='project@project.com')
        self.project2 = Experiment.objects.create(
            name='Project 2', email='project2@project.com')

    def test_valid_delete_experiment(self):
        response = client.delete(
            reverse('get_delete_update_experiment', kwargs={'pk': self.project2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_puppy(self):
        response = client.delete(
            reverse('get_delete_update_experiment', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
