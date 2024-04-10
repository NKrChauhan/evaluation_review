from rest_framework import serializers
from .models import Review, ReviewDetail


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewDetail
        fields = '__all__'
