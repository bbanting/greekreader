"""greekreader api URL configuration"""
from django.urls import path
from . import views


urlpatterns = [
    path("helpsets/", views.HelpSetList.as_view(), name="list-create-helpset"),
    path("helpsets/<int:pk>/", views.HelpSetDetail.as_view(), name="helpset-detail"),
    path("books/", views.BookList.as_view(), name="list-books"),
    path("books/<int:pk>", views.BookDetail.as_view(), name="book-detail"),
    path("roots/", views.RootList.as_view(), name="list-roots"),
    path("roots/<int:pk>", views.RootDetail.as_view(), name="root-detail"),
    path("lexemes/", views.LexemeList.as_view(), name="list-lexemes"),
    path("lexemes/<int:pk>", views.LexemeDetail.as_view(), name="lexeme-detail"),
    path("words/", views.WordList.as_view(), name="list-words"),
    path("words/<int:pk>", views.WordDetail.as_view(), name="word-detail"),
    path("words/<text>", views.WordHelp.as_view(), name="word-help"),
]
