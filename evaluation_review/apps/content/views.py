from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.review.services.review import ReviewService
from .permissions import AuthorPermission
from .models import Content
from .serializers import ContentSerializer


class ContentUploadView(generics.CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [AuthorPermission]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)


class ContentUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [AuthorPermission]

    def perform_update(self, serializer):
        serializer.save(uploaded_by=self.request.user)


class ContentReviewStatusView(generics.RetrieveAPIView):
    queryset = Content.objects.all()
    permission_classes = [AuthorPermission]
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        review_details = ReviewService.get_review_details(instance)
        
        review_status = {}
        for detail in review_details:
            review_status[detail.guideline.title] = detail.passed
        
        return Response(review_status)
