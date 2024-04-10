from rest_framework.permissions import BasePermission


class ReviewerPermission(BasePermission):
    def has_permission(self, request, view):
        return True
