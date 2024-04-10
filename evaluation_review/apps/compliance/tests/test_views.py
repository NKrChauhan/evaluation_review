from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from apps.compliance.models import Guideline


class GuidelineAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_guideline(self):
        url = reverse('guidelines-list')
        data = {'title': 'Test Guideline', 'description': 'Test description'}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Guideline.objects.count(), 1)
        self.assertEqual(Guideline.objects.get().title, 'Test Guideline')

    def test_get_guidelines_list(self):
        Guideline.objects.create(title='Guideline 1', description='Description 1')
        Guideline.objects.create(title='Guideline 2', description='Description 2')
        url = reverse('guidelines-list')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_guideline(self):
        guideline = Guideline.objects.create(title='Old Guideline', description='Old description')
        url = reverse('guideline-detail', kwargs={'pk': guideline.pk})
        updated_data = {'title': 'New Guideline', 'description': 'New description'}

        response = self.client.put(url, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Guideline.objects.get(pk=guideline.pk).title, 'New Guideline')

    def test_delete_guideline(self):
        guideline = Guideline.objects.create(title='Test Guideline', description='Test description')
        url = reverse('guideline-detail', kwargs={'pk': guideline.pk})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Guideline.objects.count(), 0)
