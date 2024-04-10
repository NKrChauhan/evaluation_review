from rest_framework import serializers
from .models import Content


class ContentSerializer(serializers.ModelSerializer):
    file = serializers.FileField(use_url=False)
    
    class Meta:
        model = Content
        fields = ('id', 'file', 'uploaded_at', 'uploaded_by')
