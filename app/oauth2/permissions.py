from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


class IsAuthenticatedPermission(BasePermission):
    """Allows access only to logged-in users."""

    def has_permission(self, request, view):
        if not request.session.get("user_id"):
            raise PermissionDenied("You must be logged in to access the API.")
        return True
