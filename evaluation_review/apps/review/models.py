from django.db import models
from django.contrib.auth.models import User
from apps.content.models import Content
from apps.compliance.models import Guideline
from django.contrib.auth.models import User


class Review(models.Model):
    # Null = True is used since there is no authentication being set up yet
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['reviewer', 'content']

    def __str__(self):
        return f"Review by {self.reviewer.username} for {self.content}"


class ReviewDetail(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    guideline = models.ForeignKey(Guideline, on_delete=models.CASCADE)
    passed = models.BooleanField(default=False)

    def __str__(self):
        return f"Review: {self.review.id}, Guideline: {self.guideline.title}, Passed: {self.passed}"
