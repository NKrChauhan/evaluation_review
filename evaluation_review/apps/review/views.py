from rest_framework import generics
from .models import Review, ReviewDetail
from .serializers import ReviewSerializer, ReviewDetailSerializer
from .permissions import ReviewerPermission


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewerPermission]


class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewerPermission]


class ReviewDetailListCreateView(generics.ListCreateAPIView):
    queryset = ReviewDetail.objects.all()
    serializer_class = ReviewDetailSerializer
    permission_classes = [ReviewerPermission]

