from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from apps.review.permissions import ReviewerPermission
from apps.content.services.content import ContentService
from apps.compliance.services.guideline import GuidelineService
from .models import ReviewDetail
from .serializers import ContentReviewDetailSerializer, ReviewSerializer, ReviewDetailSerializer


class ReviewCreateWithDetailAPIView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [ReviewerPermission]

    def create(self, request, *args, **kwargs):
        content_id = request.data.get('content_id')
        guideline_id = request.data.get('guideline')
        passed = request.data.get('passed')

        if content_id is None or guideline_id is None or passed is None:
            return Response({'error': 'content_id, guideline, and passed are required fields'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            content = ContentService.get_contnet_by_id(content_id)
        except ValueError as e:
            return Response({'error': 'Content does not exist'}, status=status.HTTP_404_NOT_FOUND)

        try:
            guideline = GuidelineService.get_guideline_by_id(guideline_id)
        except ValueError as e:
            return Response({'error': 'Guideline does not exist'}, status=status.HTTP_404_NOT_FOUND)

        review_data = {
            'reviewer': request.user.id if request.user.is_authenticated else None,
            'content': content.id,
        }
        review = self.__save_review_data(review_data)

        review_detail_data = {
            'review': review.id,
            'guideline': guideline.id,
            'passed': passed
        }
        review_detail_serializer = ReviewDetailSerializer(data=review_detail_data)
        review_detail_serializer.is_valid(raise_exception=True)
        review_detail_serializer.save()

        return Response(review_detail_serializer.data, status=status.HTTP_201_CREATED)

    def __save_review_data(self, data):
        review_serializer = self.get_serializer(data=data)
        review_serializer.is_valid(raise_exception=True)
        review = review_serializer.save()
        return review

class ReviewDetailUpdateAPIView(generics.UpdateAPIView):
    queryset = ReviewDetail.objects.all()
    serializer_class = ReviewDetailSerializer
    permission_classes = [ReviewerPermission]


class ContentReviewDetailAPIView(generics.ListAPIView):
    serializer_class = ContentReviewDetailSerializer

    def get_queryset(self):
        return ContentService.get_all_content()