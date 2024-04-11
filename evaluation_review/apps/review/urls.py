from django.urls import path
from .views import ContentReviewDetailAPIView, ReviewCreateWithDetailAPIView, ReviewDetailUpdateAPIView

urlpatterns = [
    path('create/', ReviewCreateWithDetailAPIView.as_view(), name='create-review-with-detail'),
    path('update/<int:pk>/', ReviewDetailUpdateAPIView.as_view(), name='update-review-detail'),
    path('content-review-detail/', ContentReviewDetailAPIView.as_view(), name='content-review-detail'),

]
