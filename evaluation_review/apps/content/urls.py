from django.urls import path
from .views import ContentUpdateView, ContentUploadView

urlpatterns = [
    path('upload/', ContentUploadView.as_view(), name='content-upload'),
    path('update/<int:pk>/', ContentUpdateView.as_view(), name='content-update'),
]
