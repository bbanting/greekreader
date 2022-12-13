from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin


class EditorView(TemplateView, UserPassesTestMixin):
    http_method_names = ["get", "head", "options"]
    template_name = "editor/dist/index.html"

    def test_func(self) -> bool:
        user = self.request.user
        return user.is_authenticated and user.is_staff


class ReaderView(TemplateView):
    http_method_names = ["get", "head", "options"]
    template_name = "reader/dist/index.html"
