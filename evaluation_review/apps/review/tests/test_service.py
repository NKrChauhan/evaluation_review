from django.test import TestCase
from django.contrib.auth.models import User
from apps.content.models import Content
from apps.review.models import ReviewDetail, Review
from apps.compliance.models import Guideline
from review.services.review import ReviewService


class ReviewServiceTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.content = Content.objects.create(file='test_content.txt', uploaded_by=self.user)
        self.guidelines = Guideline.objects.create(title='Test Guideline', description='Test Description')

    def test_get_review_details(self):
        review = Review.objects.create(reviewer=self.user, content=self.content)
        ReviewDetail.objects.create(review=review, guideline=self.guidelines, passed=False)
        review_details = ReviewService.get_review_details(self.content)

        self.assertEqual(len(review_details), 1)
        self.assertEqual(review_details[0].review.reviewer, self.user)
        self.assertEqual(review_details[0].passed, False)
