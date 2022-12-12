from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """The user is an admin and logged in."""
    def has_permission(self, request, view):
        return bool(
            request.user.is_staff and
            request.user.is_authenticated
        )


class EditorView(TemplateView, PermissionRequiredMixin):
    http_method_names = ["get", "head", "options"]
    template_name = "editor/dist/index.html"
