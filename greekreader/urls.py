"""greekreader root URL configuration"""
from django.contrib import admin
from django.urls import path, include

import api.views, api.urls


urlpatterns = [
    path("login/", api.views.Login.as_view(), name="login"),
    path("logout/", api.views.Logout.as_view(), name="logout"),
    path('admin/', admin.site.urls),
    path("api/", include(api.urls)),
]
