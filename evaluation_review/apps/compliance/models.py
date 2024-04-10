from django.db import models


class Guideline(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'compliance'
