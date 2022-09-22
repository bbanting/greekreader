from rest_framework import serializers

from .models import BookAccess, BookPurchase, HelpSet, Root, Lexeme, Word, Book, Collection, HelpImage, Chapter


class HelpSetSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = HelpSet
        fields = "__all__"


class BookSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "name", "cover_image"]


class ChapterSerializer(serializers.ModelSerializer):
    book = BookSerializerList()

    class Meta:
        model = Chapter
        fields = ["book", "ordinal_text", "heading", "content"]


class BookSerializerAdmin(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"
        

class BookSerializerTeacher(serializers.ModelSerializer):
    ...


class BookSerializerStudent(serializers.Serializer):
    id = serializers.IntegerField(source="book.pk")
    name = serializers.CharField(source="book.name")
    chapters = ChapterSerializer()


class CollectionSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = "__all__"


class RootSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Root
        fields = "__all__"


class LexemeSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Lexeme
        # fields = "__all__"
        exclude = ["help_images"]


class WordSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = "__all__"
        

class HelpImageSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = HelpImage
        fields = "__all__"


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["name", "books"]


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
