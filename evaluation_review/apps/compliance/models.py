from django.db import models
from django.contrib.auth.models import User


class Guideline(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # Null = True is used since there is no authentication being set up yet
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'compliance'
