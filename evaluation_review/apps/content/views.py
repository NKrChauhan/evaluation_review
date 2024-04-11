from rest_framework import generics, status
from rest_framework.response import Response
from apps.review.services.review import ReviewService
from .permissions import AuthorPermission
from .models import Content
from .serializers import ContentSerializer


class ContentUploadView(generics.CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [AuthorPermission]

    def perform_create(self, serializer):
        if not self.request.user.is_anonymous:
            serializer.save(uploaded_by=self.request.user)
        else:
            serializer.save()


class ContentUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [AuthorPermission]

    def perform_update(self, serializer):
        if not self.request.user.is_anonymous:
            serializer.save(uploaded_by=self.request.user)
        else:
            serializer.save()


class ContentReviewStatusView(generics.RetrieveAPIView):
    queryset = Content.objects.all()
    permission_classes = [AuthorPermission]
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        review_details = ReviewService.get_review_details(instance)
        print(review_details)
        review_status = []
        for detail in review_details:
            review_status.append({
                'guideline_title': detail.guideline.title,
                'status': detail.passed,
                'guideline_description': detail.guideline.description
                })
        if len(review_status) == 0:
            review_status.append({'message': 'No guideline found'})

        return Response(review_status)
