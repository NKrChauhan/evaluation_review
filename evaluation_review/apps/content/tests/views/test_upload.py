from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.content.models import Content


class ContentUploadAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client.force_authenticate(user=self.user)

    def test_content_upload(self):
        url = reverse('content-upload')
        file_content = b'Test file content to create'
        file = SimpleUploadedFile('test_file.txt', file_content, content_type='text/plain')
        data = {'file': file}

        response = self.client.post(url, data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Content.objects.filter(id=response.data.get('id')).exists())
