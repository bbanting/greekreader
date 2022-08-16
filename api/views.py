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
    """View or modify one particular helpset."""
    queryset = models.HelpSet.objects.all()
    serializer_class = serializers.HelpSetSerializer


class BookList(generics.ListCreateAPIView):
    """List books or create a new book."""
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """View or modifiy one particular book."""
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class RootList(generics.ListCreateAPIView):
    """List roots or create a new root."""
    queryset = models.Root.objects.all()
    serializer_class = serializers.RootSerializer


class RootDetail(generics.RetrieveUpdateDestroyAPIView):
    """View or modifiy one particular root."""
    queryset = models.Root.objects.all()
    serializer_class = serializers.RootSerializer


class LexemeList(generics.ListCreateAPIView):
    """List lexemes or create a lexeme book."""
    queryset = models.Lexeme.objects.all()
    serializer_class = serializers.LexemeSerializer


class LexemeDetail(generics.RetrieveUpdateDestroyAPIView):
    """View or modifiy one particular lexeme."""
    queryset = models.Lexeme.objects.all()
    serializer_class = serializers.LexemeSerializer


class WordList(generics.ListCreateAPIView):
    """List words or create a new word."""
    queryset = models.Word.objects.all()
    serializer_class = serializers.WordSerializer


class WordDetail(generics.RetrieveUpdateDestroyAPIView):
    """View or modifiy one particular word."""
    queryset = models.Word.objects.all()
    serializer_class = serializers.WordSerializer
    