from rest_framework import serializers

from .models import HelpSet, Root, Lexeme, Word, Book


class HelpSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpSet
        fields= ["name", "date_created", "creator"]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["name", "text", "date_created", "creator"]


class RootSerializer(serializers.ModelSerializer):
    class Meta:
        model = Root
        fields = ["text", "helpset", "date_created", "creator"]


class LexemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lexeme
        fields = ["text", "helpset", "root", "help_text", "help_image", "date_created", "creator"]


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ["word", "helpset", "lexeme", "parse_data", "date_created", "creator"]
        