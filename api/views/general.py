import urllib

from django.http import Http404

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .. import models, serializers



class IsAdminOrReadOnly(permissions.BasePermission):
    """The user is an admin or the method is safe."""
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user.is_staff and
            request.user.is_authenticated
        )


class UserMayAccessBook(permissions.BasePermission):
    """Tells whether the user has access to view the book."""
    def has_object_permission(self, request, view, obj):
        if type(obj) is models.Chapter:
            obj = obj.book

        for x in request.user.studygroups.all():
            if obj in x.books.all():
                return True
        return False


class LibraryView(APIView):
    """List the books available to the user."""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None) -> Response:
        """Return all the 'book shelves' for the groups the user is
        a member of."""
        groups = request.user.studygroups.all()
        serializer = serializers.StudyGroupSerializer(groups, many=True)
        return Response(serializer.data)
    

class BookView(generics.RetrieveAPIView):
    """View one book."""
    permission_classes = [UserMayAccessBook]
    serializer_class = serializers.BookSerializer
    queryset = models.Book.objects.all()
    lookup_field = "pk"


class ChapterView(generics.RetrieveAPIView):
    """View one chapter."""
    permission_classes = [UserMayAccessBook]
    serializer_class = serializers.ChapterSerializer
    queryset = models.Chapter.objects.all()
    lookup_field = "pk"


class WordHelp(generics.ListAPIView):
    """Displays help for a word form to the reader."""
    permission_classes = [UserMayAccessBook]
    serializer_class = serializers.WordSerializer
    http_method_names = ["get", "head"]

    def get_queryset(self):
        """Search for the word in all relevant helpsets; return first match."""
        helpsets = self.get_book(self.kwargs["bookid"]).helpsets.all()
        word_text = urllib.parse.unquote(self.kwargs["text"])

        for hs in helpsets:
            if words := models.Word.objects.filter(text=word_text, helpset=hs):
                return words
        raise Http404()

    def get_book(self, id) -> models.Book:
        """Return the book after checking if it exists and
        the user has permission to read it."""
        try:
            book = models.Book.objects.get(pk=id)
        except models.Book.DoesNotExist:
            raise Http404()
        else:
            self.check_object_permissions(self.request, book)
            return book

    def get(self, request, format=None) -> Response:
        words = self.get_queryset()
        serializer = self.serializer_class(words, many=True)
        return Response(serializer.data)


class StudyGroupListView(generics.ListAPIView):
    """Displays the list of study groups belonging to user."""
    serializer_class = serializers.StudyGroupSerializer
    queryset = models.StudyGroup.objects.all()
    lookup_field = "pk"
    http_method_names = ["get", "head", "options"]
    

class StudyGroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Displays a single study group."""
    serializer_class = serializers.StudyGroupSerializer
    queryset = models.StudyGroup.objects.all()
    lookup_field = "pk"
    http_method_names = ["get", "head", "options", "post", "put", "patch", "delete"]
