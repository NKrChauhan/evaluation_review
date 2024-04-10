from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import AuthorPermission
from .models import Content
from .serializers import ContentSerializer


class ContentUploadView(generics.CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticated, AuthorPermission]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

class ContentUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticated, AuthorPermission]

    def perform_update(self, serializer):
        serializer.save(uploaded_by=self.request.user)
