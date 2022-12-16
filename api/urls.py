"""greekreader api URL configuration"""
from django.urls import path, include
from . import views


admin_only = [
    path("helpsets/", views.HelpSetList.as_view(), name="list-create-helpset"),
    path("helpsets/<int:pk>/", views.HelpSetDetail.as_view(), name="helpset-detail"),
    path("helpsetsettings/<int:pk>/", views.HelpSetSettingsDetail.as_view(), name="helpset-settings-detail"),
    path("roots/", views.RootList.as_view(), name="list-roots"),
    path("roots/<int:pk>/", views.RootDetail.as_view(), name="root-detail"),
    path("lexemes/", views.LexemeList.as_view(), name="list-lexemes"),
    path("lexemes/<int:pk>/", views.LexemeDetail.as_view(), name="lexeme-detail"),
    path("words/", views.WordList.as_view(), name="list-words"),
    path("words/<int:pk>/", views.WordDetail.as_view(), name="word-detail"),
    path("books/", views.BookList.as_view(), name="list-books"),
    path("books/<int:pk>/", views.BookDetail.as_view(), name="book-detail"),
    path("chapters/", views.ChapterList.as_view(), name="list-chapters"),
    path("chapters/<int:pk>/", views.ChapterDetail.as_view(), name="chapter-detail"),
    path("helpimages/", views.HelpImageList.as_view(), name="list-helpimages"),
    path("helpimages/<int:pk>/", views.HelpImageDetail.as_view(), name="helpimage-detail"),
    path("studygroups/", views.StudyGroupList.as_view(), name="list-studygroups"),
    path("studygroups/<int:pk>/", views.StudyGroupDetail.as_view(), name="studygroup-detail"),
]

urlpatterns = [
    path("books/", views.LibraryView.as_view(), name="library"),
    path("books/<int:pk>/", views.BookView.as_view(), name="book-view"),
    path("chapters/<int:pk>/", views.ChapterView.as_view(), name="chapter-view"),
    path("words/<int:bookid>/<text>/", views.HelpView.as_view(), name="word-help"),
    path("edit/", include(admin_only))
]
