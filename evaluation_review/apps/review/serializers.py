from rest_framework import serializers
from .models import Review, ReviewDetail
from apps.content.models import Content


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'reviewer', 'content', 'created_at']
        read_only_fields = ['id', 'reviewer', 'created_at']

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewDetail
        fields = ['id', 'review', 'guideline', 'passed']

class ContentReviewDetailSerializer(serializers.ModelSerializer):
    # Serializer for ReviewDetail model
    review_detail = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = ['id', 'file', 'uploaded_at', 'uploaded_by', 'review_detail']

    def get_review_detail(self, obj):
        review_details = ReviewDetail.objects.filter(review__content=obj)
        return ReviewDetailSerializer(review_details, many=True).data
