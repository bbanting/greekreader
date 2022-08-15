from rest_framework import serializers

from .models import HelpSet, Root, Lexeme, Link, Book


class HelpSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpSet
        fields= ["name", "date_created", "creator"]
        