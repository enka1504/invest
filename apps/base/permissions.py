# permissions.py

from rest_framework.permissions import BasePermission

class PublicAccessPermission(BasePermission):
    """
    Allow public access to certain views.
    """
    def has_permission(self, request, view):
        return True  # Allow access to all users (authenticated or not)
