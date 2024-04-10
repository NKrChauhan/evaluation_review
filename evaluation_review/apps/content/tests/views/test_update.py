from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from apps.content.models import Content
from django.core.files.uploadedfile import SimpleUploadedFile


class ContentUpdateAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client.force_authenticate(user=self.user)

    def test_content_update(self):
        url = reverse('content-upload')
        file_content = b'Test file content to update'
        file = SimpleUploadedFile('test_file.txt', file_content, content_type='text/plain')
        data = {'file': file}
        upload_response = self.client.post(url, data, format='multipart')

        url = reverse('content-update', kwargs={'pk': upload_response.data.get('id')})
        updated_file_content = b'Updated test file content'
        updated_file_content = SimpleUploadedFile('test_file_1.txt', updated_file_content, content_type='text/plain')
        data = {'file': updated_file_content}

        response = self.client.put(url, data, format='multipart')

        content_data = Content.objects.filter(pk=response.data.get('id'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(content_data.exists())
        self.assertIn('test_file_1',content_data.first().file.name)
