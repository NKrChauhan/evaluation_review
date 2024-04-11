from django.urls import path
from .views import ContentUpdateView, ContentUploadView, ContentReviewStatusView

urlpatterns = [
    path('upload/', ContentUploadView.as_view(), name='content-upload'),
    path('update/<int:pk>/', ContentUpdateView.as_view(), name='content-update'),
    path('<int:pk>/review/status/', ContentReviewStatusView.as_view(), name='content-review-status'),
]
