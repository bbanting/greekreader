from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .. import models, serializers


def admin_view_factory(model, serializer) -> tuple[ListCreateAPIView, RetrieveUpdateDestroyAPIView]:
    attrs = {
        "queryset": model.objects.all(),
        "serializer_class": serializer,
        # "permission_classes": [permissions.IsAdminUser],
        }
    model_name = model.__name__

    return (
        type(
            f"{model_name}List", 
            (ListCreateAPIView,), 
            {**attrs, "__doc__": f"List current {model_name}s or create a new one."}
        ),
        type(
            f"{model_name}Detail", 
            (RetrieveUpdateDestroyAPIView,), 
            {**attrs, "__doc__": f"View or modify a {model_name}."}
        ),
    )


HelpSetList, HelpSetDetail = admin_view_factory(models.HelpSet, serializers.HelpSetSerializerAdmin)
RootList, RootDetail = admin_view_factory(models.Root, serializers.RootSerializerAdmin)
LexemeList, LexemeDetail = admin_view_factory(models.Lexeme, serializers.LexemeSerializerAdmin)
HelpImageList, HelpImageDetail = admin_view_factory(models.HelpImage, serializers.HelpImageSerializerAdmin)
WordList, WordDetail = admin_view_factory(models.WordLink, serializers.WordSerializerAdmin)
BookList, BookDetail = admin_view_factory(models.Book, serializers.BookSerializerAdmin)
ChapterList, ChapterDetail = admin_view_factory(models.Chapter, serializers.ChapterSerializerAdmin)
StudyGroupList, StudyGroupDetail = admin_view_factory(models.StudyGroup, serializers.StudyGroupSerializerAdmin)
_, HelpSetSettingsDetail = admin_view_factory(models.HelpSetSettings, serializers.HelpSetSettingsSerializerAdmin)
