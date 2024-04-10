from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from apps.review.models import Review, ReviewDetail
from apps.content.models import Content
from apps.compliance.models import Guideline

class ReviewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.content = Content.objects.create(file='test_content.txt')
        self.guideline = Guideline.objects.create(title='Test Guideline', description='Test Description')

    def test_create_review(self):
        url = reverse('review-list-create')
        data = {'reviewer': self.user.id, 'content': self.content.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Review.objects.filter(content=self.content, reviewer=self.user).exists())

    def test_get_review_list(self):
        Review.objects.create(reviewer=self.user, content=self.content)
        url = reverse('review-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_review_detail(self):
        review = Review.objects.create(reviewer=self.user, content=self.content)
        url = reverse('review-detail', kwargs={'pk': review.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['reviewer'], self.user.id)

    def test_create_review_detail(self):
        review = Review.objects.create(reviewer=self.user, content=self.content)
        url = reverse('review-detail-list-create')
        data = {'review': review.id, 'guideline': self.guideline.id, 'passed': True}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(ReviewDetail.objects.filter(review=review, guideline=self.guideline, passed=True).exists())

    def test_get_review_detail_list(self):
        review = Review.objects.create(reviewer=self.user, content=self.content)
        ReviewDetail.objects.create(review=review, guideline=self.guideline, passed=True)
        url = reverse('review-detail-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
