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


class UserMayAccessStudyGroup(permissions.BasePermission):
    """Tells whether the user has access to view and edit a study group."""
    def has_object_permission(self, request, view, obj):
        memberships = self.request.user.memberships.prefetch_related("studygroup").filter(is_teacher=True)
        for m in memberships:
            if obj == m.studygroup:
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


class HelpView(generics.ListAPIView):
    """Displays help for a word form to the reader."""
    permission_classes = [UserMayAccessBook]
    serializer_class = serializers.WordSerializer
    http_method_names = ["get", "head", "options"]

    def get_queryset(self):
        """Search for the word in all relevant helpsets; return first match."""
        book = self.get_book(self.kwargs["bookid"])
        helpset, fallback = book.helpset, book.fallback_helpset
        word_text = urllib.parse.unquote(self.kwargs["text"])

        if words := models.Word.objects.filter(text=word_text, helpset=helpset):
            return words
        elif words := models.Word.objects.filter(text=word_text, helpset=fallback):
            return words
        else:
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
    lookup_field = "pk"
    http_method_names = ["get", "head", "options"]

    def get_queryset(self):
        """Get the studygroups for which user is a teacher."""
        memberships = self.request.user.memberships.prefetch_related("studygroup").filter(is_teacher=True)
        return [m.studygroup for m in memberships]
    

class StudyGroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Displays a single study group."""
    permission_classes = [UserMayAccessStudyGroup]
    serializer_class = serializers.StudyGroupSerializer
    queryset = models.StudyGroup.objects.all()
    lookup_field = "pk"
    http_method_names = ["get", "head", "options", "post", "put", "patch", "delete"]
