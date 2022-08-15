"""greekreader api URL configuration"""
from django.urls import path
from . import views


urlpatterns = [
    path("helpsets/", views.HelpSetList.as_view(), name="list-create-helpset"),
    path("helpsets/<int:pk>/", views.HelpSetDetail.as_view(), name="helpset-detail"),
]
