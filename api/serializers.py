from rest_framework import serializers

from .models import HelpSet, Root, Lexeme, Word, Book, Collection, HelpImage


### ADMIN SERIALIZERS

class HelpSetSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = HelpSet
        fields = "__all__"


class BookSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


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
        

### NORMAL SERIALIZERS

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["name", "text"]


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["name", "books"]


class HelpImageSerializer(serializers.Serializer):
    url = serializers.ImageField(source="image")


class LexemeSerializer(serializers.Serializer):
    text = serializers.CharField()
    help_text = serializers.CharField(allow_blank=True)
    help_images = HelpImageSerializer(many=True)


class WordSerializer(serializers.Serializer):
    text = serializers.CharField()
    lexeme = LexemeSerializer()
    parse_data = serializers.CharField(allow_blank=True)
