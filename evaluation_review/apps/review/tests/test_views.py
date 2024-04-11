from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.review.models import Review, ReviewDetail
from apps.content.models import Content
from apps.compliance.models import Guideline


class ReviewCreateWithDetailAPITests(APITestCase):
    def setUp(self):
        self.content = Content.objects.create(file="test_content.txt")
        self.guideline = Guideline.objects.create(title="Example Guideline", description="Example description")

        self.content_id = self.content.id
        self.guideline_id = self.guideline.id
        self.passed = False

    def test_create_review_with_detail(self):
        url = reverse('create-review-with-detail')
        data = {
            "content_id": self.content_id,
            "guideline": self.guideline_id,
            "passed": self.passed
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(ReviewDetail.objects.count(), 1)

    def test_create_review_with_detail_invalid_data(self):
        url = reverse('create-review-with-detail')
        data = {
            "content_id": None,  # Invalid data
            "guideline": self.guideline_id,
            "passed": self.passed
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Review.objects.count(), 0)
        self.assertEqual(ReviewDetail.objects.count(), 0)


class ReviewDetailUpdateAPITests(APITestCase):
    def setUp(self):
        self.content = Content.objects.create(file="test_content.txt")
        self.guideline = Guideline.objects.create(title="Example Guideline", description="Example description")
        self.review = Review.objects.create(content_id=self.content.id)
        self.content_id = self.content.id
        self.guideline_id = self.guideline.id

        self.review_detail = ReviewDetail.objects.create(review_id=self.review.id, guideline_id=self.guideline.id, passed=False)
        self.valid_payload = {
            "passed": True
        }
        self.invalid_payload = {
            "passed": None  # Invalid payload
        }

    def test_update_review_detail(self):
        url = reverse('update-review-detail', kwargs={'pk': self.review_detail.id})

        response = self.client.patch(url, self.valid_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.review_detail.refresh_from_db()
        self.assertTrue(self.review_detail.passed)

    def test_update_review_detail_invalid_data(self):
        url = reverse('update-review-detail', kwargs={'pk': self.review_detail.id})

        response = self.client.patch(url, self.invalid_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class ContentReviewDetailAPITests(APITestCase):
    def setUp(self):
        self.guideline = Guideline.objects.create(title="Example Guideline", description="Example description")

        self.content1 = Content.objects.create(file="test_content_1.txt")
        self.content2 = Content.objects.create(file="test_content_2.txt")

        self.review_1 = Review.objects.create(content_id=self.content1.id)
        self.review_2 = Review.objects.create(content_id=self.content2.id)

        self.review_detail1 = ReviewDetail.objects.create(review_id=self.review_1.id, guideline_id=self.guideline.id, passed=False)
        self.review_detail2 = ReviewDetail.objects.create(review_id=self.review_2.id, guideline_id=self.guideline.id, passed=True)


    def test_get_content_review_detail(self):
        url = reverse('content-review-detail')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Assuming there are two content objects in the database
        # Asserting content data
        self.assertEqual(response.data[0]['id'], self.content1.id)
        self.assertEqual(response.data[1]['id'], self.content2.id)
        # Asserting review details for the first content
        self.assertEqual(len(response.data[0]['review_detail']), 1)  # Assuming there is one review detail for the first content
        self.assertEqual(response.data[0]['review_detail'][0]['id'], self.review_detail1.id)
        # Asserting review details for the second content
        self.assertEqual(len(response.data[1]['review_detail']), 1)  # Assuming there is one review detail for the second content
        self.assertEqual(response.data[1]['review_detail'][0]['id'], self.review_detail2.id)
