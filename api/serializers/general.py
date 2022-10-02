from rest_framework import serializers

from models import Lexeme, Word, Book, Collection, Chapter


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "name"]


class ChapterSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Chapter
        fields = ["book", "order", "ordinal_text", "title", "content"]


class ChapterSerializerMin(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Chapter
        fields = ["book", "order", "ordinal_text", "title"]


class BookSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializerMin(many=True)

    class Meta:
        model = Book
        fields = ["id", "name", "cover_image", "chapters"]


class HelpImageSerializer(serializers.Serializer):
    url = serializers.ImageField(source="image")
    title = serializers.CharField(max_length=100)


class LexemeSerializer(serializers.Serializer):
    text = serializers.CharField()
    help_text = serializers.CharField(allow_blank=True)
    help_images = HelpImageSerializer(many=True)


class WordSerializer(serializers.Serializer):
    text = serializers.CharField()
    lexeme = LexemeSerializer()
    parse_data = serializers.CharField(allow_blank=True)


class StudyGroupSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    shelf = BookSerializer(many=True)
    