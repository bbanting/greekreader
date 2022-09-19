from django.http import Http404
from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers, models


class IsAdminOrReadOnly(permissions.BasePermission):
    """The user is an admin or the method is safe."""
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user.is_staff and
            request.user.is_authenticated
        )


class HelpSetList(generics.ListCreateAPIView):
    """List current helpsets or create a new helpset."""
    queryset = models.HelpSet.objects.all()
    serializer_class = serializers.HelpSetSerializerAdmin
    permission_classes = [permissions.IsAdminUser]


class HelpSetDetail(generics.RetrieveUpdateDestroyAPIView):
    """View or modify one particular helpset."""
    queryset = models.HelpSet.objects.all()
    serializer_class = serializers.HelpSetSerializerAdmin
    permission_classes = [permissions.IsAdminUser]


class BookList(generics.ListCreateAPIView):
    """List books or create a new book."""
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return self.request.user.profile.books.all()

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return serializers.BookSerializerAdmin
        else:
            return serializers.BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """View or modifiy one particular book."""
    queryset = models.Book.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return self.request.user.profile.books.all()
    
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return serializers.BookSerializerAdmin
        else:
            return serializers.BookSerializer


class RootList(generics.ListCreateAPIView):
    """List roots or create a new root."""
    queryset = models.Root.objects.all()
    serializer_class = serializers.RootSerializerAdmin
    permission_classes = [permissions.IsAdminUser]


class RootDetail(generics.RetrieveUpdateDestroyAPIView):
    """View or modifiy one particular root."""
    queryset = models.Root.objects.all()
    serializer_class = serializers.RootSerializerAdmin
    permission_classes = [permissions.IsAdminUser]


class LexemeList(generics.ListCreateAPIView):
    """List lexemes or create a lexeme book."""
    queryset = models.Lexeme.objects.all()
    serializer_class = serializers.LexemeSerializerAdmin
    permission_classes = [permissions.IsAdminUser]


class LexemeDetail(generics.RetrieveUpdateDestroyAPIView):
    """View or modifiy one particular lexeme."""
    queryset = models.Lexeme.objects.all()
    serializer_class = serializers.LexemeSerializerAdmin
    permission_classes = [permissions.IsAdminUser]


class WordList(generics.ListCreateAPIView):
    """List words or create a new word."""
    queryset = models.Word.objects.all()
    serializer_class = serializers.WordSerializer
    permission_classes = [permissions.IsAdminUser]


class WordDetail(generics.RetrieveUpdateDestroyAPIView):
    """View or modifiy one particular word."""
    queryset = models.Word.objects.all()
    serializer_class = serializers.WordSerializerAdmin
    permission_classes = [permissions.IsAdminUser]


class WordHelp(generics.ListAPIView):
    """Displays help for a word form to the reader."""
    serializer_class = serializers.WordSerializer
    http_method_names = ["get", "head"]

    def get_queryset(self):
        """Search for the word in all relevant helpsets; return first match."""
        helpsets = models.Book.objects.get(pk=self.kwargs["bookid"]).helpsets.all()
        for hs in helpsets:
            if words := models.Word.objects.filter(text=self.kwargs["text"], helpset=hs):
                return words
        raise Http404()
