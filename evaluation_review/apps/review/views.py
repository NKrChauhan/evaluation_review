from rest_framework import generics
from .models import Review, ReviewDetail
from .serializers import ReviewSerializer, ReviewDetailSerializer


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailListCreateView(generics.ListCreateAPIView):
    queryset = ReviewDetail.objects.all()
    serializer_class = ReviewDetailSerializer
