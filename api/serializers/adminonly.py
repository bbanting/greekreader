from rest_framework import serializers

from ..models import (HelpSet, Root, Lexeme, WordLink, 
                    Book, Collection, HelpImage, 
                    Chapter, Parsing, StudyGroup, HelpSetSettings)


class HelpSetSerializerAdmin(serializers.ModelSerializer):
    settings = serializers.PrimaryKeyRelatedField(queryset=HelpSetSettings.objects.all())

    class Meta:
        model = HelpSet
        fields = "__all__"


class HelpSetSettingsSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = HelpSetSettings
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
    chapters = ChapterSerializerAdmin(many=True)
    
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
    help_images = serializers.PrimaryKeyRelatedField(many=True, queryset=HelpImage.objects.all())

    class Meta:
        model = Lexeme
        fields = "__all__"


class WordSerializerAdmin(serializers.ModelSerializer):
    parsings = serializers.PrimaryKeyRelatedField(many=True, queryset=Parsing.objects.all())

    class Meta:
        model = WordLink
        fields = "__all__"


class StudyGroupSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = "__all__"
        