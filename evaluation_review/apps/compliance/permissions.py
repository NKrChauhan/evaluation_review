from rest_framework.permissions import BasePermission


class ComplianceUserPermission(BasePermission):
    def has_permission(self, request, view):
        return True
