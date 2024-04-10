from rest_framework import generics

from .permissions import ComplianceUserPermission
from .models import Guideline
from .serializers import GuidelineSerializer


class GuidelineListView(generics.ListCreateAPIView):
    queryset = Guideline.objects.all()
    serializer_class = GuidelineSerializer
    permission_classes = [ComplianceUserPermission]


class GuidelineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guideline.objects.all()
    serializer_class = GuidelineSerializer
    permission_classes = [ComplianceUserPermission]
