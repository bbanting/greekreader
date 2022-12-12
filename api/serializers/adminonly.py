from rest_framework import serializers

from ..models import HelpSet, Root, Lexeme, Word, Book, Collection, HelpImage, Chapter, Parsing


class HelpSetSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = HelpSet
        fields = "__all__"


class CollectionSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = "__all__"


class ChapterSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = "__all__"


class BookSerializerAdmin(serializers.ModelSerializer):
    chapters = serializers.PrimaryKeyRelatedField(many=True, queryset=Chapter.objects.all())

    class Meta:
        model = Book
        fields = "__all__"
        

class HelpImageSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = HelpImage
        fields = "__all__"


class RootSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Root
        fields = "__all__"


class ParsingSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Parsing
        fields = "__all__"


class LexemeSerializerAdmin(serializers.ModelSerializer):
    help_images = HelpImageSerializerAdmin(many=True)

    class Meta:
        model = Lexeme
        fields = "__all__"


class WordSerializerAdmin(serializers.ModelSerializer):
    parsings = ParsingSerializerAdmin(many=True)
    
    class Meta:
        model = Word
        fields = "__all__"
