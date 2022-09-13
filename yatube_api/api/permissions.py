# yatube_api/api/permissions.py
from rest_framework import permissions


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method is permissions.SAFE_METHODS
            or obj.author == request.user
        )
