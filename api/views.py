from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers, models


class HelpSetList(generics.ListCreateAPIView):
    """List current helpsets or create a new helpset."""
    queryset = models.HelpSet.objects.all()
    serializer_class = serializers.HelpSetSerializer


class HelpSetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.HelpSet.objects.all()
    serializer_class = serializers.HelpSetSerializer
    