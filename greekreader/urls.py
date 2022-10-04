"""greekreader root URL configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

import api.urls
import accounts.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(api.urls)),
    path("", include(accounts.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
