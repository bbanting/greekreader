import collections
from rest_framework import serializers

from .models import BookAccess, BookPurchase, HelpSet, Root, Lexeme, Word, Book, Collection, HelpImage, Chapter


class HelpSetSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = HelpSet
        fields = "__all__"


class BookSerializerMin(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "name", "cover_image"]


class ChapterSerializer(serializers.ModelSerializer):
    book = BookSerializerMin()

    class Meta:
        model = Chapter
        fields = ["book", "order", "ordinal_text", "heading", "content"]


class ChapterSerializerMin(serializers.ModelSerializer):
    book = BookSerializerMin()

    class Meta:
        model = Chapter
        fields = ["order", "ordinal_text", "heading"]


class CollectionSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = "__all__"


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "name"]


class BookSerializerAdmin(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"
        

class BookPurchaseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="book.pk")
    name = serializers.CharField(source="book.name")
    chapters = ChapterSerializer(source="book.chapters", many=True)
    collections = CollectionSerializer(many=True)
    # collections = serializers.CharField(source="collections.name", many=True)


class BookPurchaseSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = BookPurchase
        fields = "__all__"


class BookAccessSerializer(serializers.Serializer):
    id = serializers.IntegerField(source="book.pk")
    name = serializers.CharField(source="book.name")
    student = serializers.PrimaryKeyRelatedField()
    chapters = ChapterSerializerMin(many=True)


class BookAccessSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = BookAccess
        fields = "__all__"


class RootSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Root
        fields = "__all__"
        

class HelpImageSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = HelpImage
        fields = "__all__"


class HelpImageSerializer(serializers.Serializer):
    url = serializers.ImageField(source="image")
    title = serializers.CharField(max_length=100)


class LexemeSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Lexeme
        # fields = "__all__"
        exclude = ["help_images"]


class LexemeSerializer(serializers.Serializer):
    text = serializers.CharField()
    help_text = serializers.CharField(allow_blank=True)
    help_images = HelpImageSerializer(many=True)


class WordSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = "__all__"


class WordSerializer(serializers.Serializer):
    text = serializers.CharField()
    lexeme = LexemeSerializer()
    parse_data = serializers.CharField(allow_blank=True)
