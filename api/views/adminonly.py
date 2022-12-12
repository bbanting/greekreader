from rest_framework import generics
from rest_framework import permissions

from .. import models, serializers


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
    """List lexemes or create a lexeme."""
    queryset = models.Lexeme.objects.all()
    serializer_class = serializers.LexemeSerializerAdmin
    permission_classes = [permissions.IsAdminUser]


class LexemeDetail(generics.RetrieveUpdateDestroyAPIView):
    """View or modifiy one particular lexeme."""
    queryset = models.Lexeme.objects.all()
    serializer_class = serializers.LexemeSerializerAdmin
    permission_classes = [permissions.IsAdminUser]
    

class HelpImageList(generics.ListCreateAPIView):
    """List help images or create one."""
    queryset = models.HelpImage.objects.all()
    serializer_class = serializers.HelpImageSerializerAdmin
    permission_classes = [permissions.IsAdminUser]
    

class HelpImageDetail(generics.RetrieveUpdateDestroyAPIView):
    """View or modify a help image."""
    queryset = models.HelpImage.objects.all()
    serializer_class = serializers.HelpImageSerializerAdmin
    permission_classes = [permissions.IsAdminUser]


class WordList(generics.ListCreateAPIView):
    """List words or create a new word."""
    queryset = models.Word.objects.all()
    serializer_class = serializers.WordSerializerAdmin
    permission_classes = [permissions.IsAdminUser]


class WordDetail(generics.RetrieveUpdateDestroyAPIView):
    """View or modifiy one particular word."""
    queryset = models.Word.objects.all()
    serializer_class = serializers.WordSerializerAdmin
    permission_classes = [permissions.IsAdminUser]


class BookList(generics.ListCreateAPIView):
    """List books or create a new book."""
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializerAdmin
    permission_classes = [permissions.IsAdminUser]


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """View or modifiy one particular book."""
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializerAdmin
    permission_classes = [permissions.IsAdminUser]


class ChapterList(generics.ListCreateAPIView):
    """List chapters or create a new chapter."""
    queryset = models.Chapter.objects.all()
    serializer_class = serializers.ChapterSerializerAdmin
    permission_classes = [permissions.IsAdminUser]


class ChapterDetail(generics.RetrieveUpdateDestroyAPIView):
    """View or modifiy one particular chapter."""
    queryset = models.Chapter.objects.all()
    serializer_class = serializers.ChapterSerializerAdmin
    permission_classes = [permissions.IsAdminUser]
