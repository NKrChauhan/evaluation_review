import os
from django.db import models
from django.contrib.auth.models import User


class Content(models.Model):
    file = models.FileField(upload_to='content_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # Null = True is used since there is no authentication being set up yet
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_contents', null=True)

    def get_filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.get_filename()

    class Meta:
        app_label = 'content'
