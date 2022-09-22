"""greekreader root URL configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

import api.views, api.urls


urlpatterns = [
    path("login/", api.views.Login.as_view(), name="login"),
    path("logout/", api.views.Logout.as_view(), name="logout"),
    path('admin/', admin.site.urls),
    path("api/", include(api.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
