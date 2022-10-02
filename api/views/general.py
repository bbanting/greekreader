from django.http import Http404

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import models, serializers



class IsAdminOrReadOnly(permissions.BasePermission):
    """The user is an admin or the method is safe."""
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user.is_staff and
            request.user.is_authenticated
        )


class LibraryView(APIView):
    """List the books available to the user."""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None) -> Response:
        groups = request.user.studygroups.all()
        serializer = serializers.StudyGroupSerializer(groups, many=True)
        return Response(serializer.data)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """View or modifiy one particular book."""
    queryset = models.Book.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        ...
        # return self.request.user.profile.books.all()
    
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return serializers.BookSerializerAdmin
        elif self.request.user.profile.is_teacher:
            return serializers.BookPurchaseSerializer
        else:
            return serializers.BookAccessSerializer


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
