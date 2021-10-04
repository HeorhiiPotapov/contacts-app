from django.http import response
from django.test import Client, TestCase
from django.urls import reverse

from contacts.api.views import ContactsSerializer
from contacts.models import Contact

from .models import Contact
from .serializers import ContactsSerializer

client = Client()


# class ContactTest(TestCase):
#     def setUp(self):
#         Contact.objects.create(name="Henry", id="1", email="genryfordman")

#     def test_contacts_model(self):
#         contacts = Contact.objects.all()
#         to_retrieve = self.contacts.get(name="Henry")
#         print(self.assertEqual(contacts, to_retrieve))

#     def test_contacts_available(self):
#         response = client.get('http://localhost:8000/contacts')
#         print(response)
#         current = Contact.objects.all().count()
#         # self.assertEqual()

#     def test_delete_contact(self):
#         response = client.delete('http://localhost:8000/contacts')
#         print(response)

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


class GetAllContactsTest(TestCase):
    """ Test module for GET all experiments API """

    def setUp(self):
        Contact.objects.create(

            name='Project', email='project@project.com')
        Contact.objects.create(

            name='Project 2', email='project2@project.com')
        Contact.objects.create(

            name='Project 3', email='project3@project.com')
        Contact.objects.create(

            name='Project 4', email='project4@project.com')

    def test_get_all_experiments(self):
        response = client.get(reverse('get_post_experiments'))
        experiments = Contact.objects.all()
        serializer = ContactSerializer(experiments, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSinglePuppyTest(TestCase):
    """ Test module for GET single puppy API """

    def setUp(self):
        self.project = Experiment.objects.create(
            name='Project', email='project@project.com', score=1)
        self.project2 = Experiment.objects.create(
            name='Project 2', email='project2@project.com', score=2)
        self.project3 = Experiment.objects.create(
            name='Project 3', email='project3@project.com', score=3)
        self.project4 = Experiment.objects.create(
            name='Project 4', email='project4@project.com', score=4)

    def test_get_valid_single_experiment(self):
        response = client.get(
            reverse('get_delete_update_experiment', kwargs={'pk': self.project2.pk}))
        experiment = Experiment.objects.get(pk=self.project2.pk)
        serializer = ExperimentSerializer(experiment)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_experiment(self):
        response = client.get(
            reverse('get_delete_update_experiment', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewExperimentTest(TestCase):
    """ Test module for inserting a new experiment """

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
            reverse('get_post_experiments'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_experiment(self):
        response = client.post(
            reverse('get_post_experiments'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleExperimentTest(TestCase):
    """ Test module for updating an existing experiment record """

    def setUp(self):
        self.project = Experiment.objects.create(
            name='Project', email='project@project.com', score=1)
        self.project2 = Experiment.objects.create(
            name='Project 2', email='project2@project.com', score=2)
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
            name='Project', email='project@project.com', score=1)
        self.project2 = Experiment.objects.create(
            name='Project 2', email='project2@project.com', score=2)

    def test_valid_delete_experiment(self):
        response = client.delete(
            reverse('get_delete_update_experiment', kwargs={'pk': self.project2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_puppy(self):
        response = client.delete(
            reverse('get_delete_update_experiment', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
