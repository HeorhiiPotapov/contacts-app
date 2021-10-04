from django.http import response
from django.urls import reverse
from django.test import Client, TestCase

from contacts.models import Contact

from .models import Contact

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


class GetAllExperimentExperiment


Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experimentTest(TestCase):
    """ Test module for GET all experiments API """

    def setUp(self):
        ExperimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment.objects.create(
            name='Project', email='project@project.com', score=1)
        ExperimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment.objects.create(
            name='Project 2', email='project2@project.com', score=2)
        ExperimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment.objects.create(
            name='Project 3', email='project3@project.com', score=3)
        ExperimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment.objects.create(
            name='Project 4', email='project4@project.com', score=4)

    def test_get_all_experimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiments(self):
        # get API response
        response = client.get(reverse('get_post_experimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiments'))
        # get data from db
        experimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiments = ExperimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment.objects.all()
        serializer = ExperimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experimentSerializer(experimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiments, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSinglePuppyTest(TestCase):
    """ Test module for GET single puppy API """

    def setUp(self):
        self.project = ExperimentExperiment


Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment.objects.create(
            name='Project', email='project@project.com', score=1)
        self.project2 = ExperimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment.objects.create(
            name='Project 2', email='project2@project.com', score=2)
        self.project3 = ExperimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment.objects.create(
            name='Project 3', email='project3@project.com', score=3)
        self.project4 = ExperimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment.objects.create(
            name='Project 4', email='project4@project.com', score=4)

    def test_get_valid_single_experiment(self):
        response = client.get(
            reverse('get_delete_update_experiment', kwargs={'pk': self.project2.pk}))
        experiment = ExperimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment.objects.get(pk=self.project2.pk)
        serializer = ExperimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experimentSerializer(experiment)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_experiment(self):
        response = client.get(
            reverse('get_delete_update_experiment', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewExperimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experimentTest(TestCase):
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
experimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
    def test_create_valid_experiment(self):
        response = client.post(
            reverse('Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_experimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment(self):
        response = client.post(
            reverse('get_post_experimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiments'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleExperimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experimentTest(TestCase):
    """ Test module for updating an existing experimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment record """

    def setUp(self):
        self.project = ExperimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment.objects.create(
            name='Project', email='project@project.com', score=1)
        self.project2 = ExperimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment.objects.create(
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

    def test_valid_update_experimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment(self):
        response = client.put(
            reverse('get_delete_update_experimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment', kwargs={'pk': self.project2.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_experimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment(self):
        response = client.put(
            reverse('get_delete_update_experimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment', kwargs={'pk': self.project2.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleExperimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experimentTest(TestCase):
    """ Test module for deleting an existing experimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment record """

    def setUp(self):
        self.project = ExperimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment.objects.create(
            name='Project', email='project@project.com', score=1)
        self.project2 = ExperimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment.objects.create(
            name='Project 2', email='project2@project.com', score=2)

    def test_valid_delete_experimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment(self):
        response = client.delete(
            reverse('get_delete_update_experimentExperiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
Experiment
Experiment
experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment
experiment
Experiment
experiment
Experiment
Experiment
experiment
experiment
experiment', kwargs={'pk': self.project2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_puppy(self):
        response = client.delete(
            reverse('get_delete_update_experiment', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
