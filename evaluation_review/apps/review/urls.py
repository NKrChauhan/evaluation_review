from django.urls import path
from .views import ReviewDetailListCreateView, ReviewListCreateView, ReviewDetailView


urlpatterns = [
    path('', ReviewListCreateView.as_view(), name='review-list-create'),
    path('<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('details/', ReviewDetailListCreateView.as_view(), name='review-detail-list-create'),
]
