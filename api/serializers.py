from rest_framework import serializers

from .models import HelpSet, Root, Lexeme, Word, Book, Collection, HelpImage, Chapter, StudyGroup


class HelpSetSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = HelpSet
        fields = "__all__"


class CollectionSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = "__all__"


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


class BookSerializerAdmin(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializerMin(many=True)

    class Meta:
        model = Book
        fields = ["id", "name", "cover_image", "chapters"]
        

class HelpImageSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = HelpImage
        fields = "__all__"


class HelpImageSerializer(serializers.Serializer):
    url = serializers.ImageField(source="image")
    title = serializers.CharField(max_length=100)


class RootSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Root
        fields = "__all__"


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
