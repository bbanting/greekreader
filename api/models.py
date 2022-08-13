from django.db import models
from django.contrib.auth.models import User


class HelpSet(models.Model):
    """A set of lexical helps."""
    name = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(User, models.SET_NULL, null=True)
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) # NOTE: Set when altering Lexeme

    def __str__(self) -> str:
        return self.name


class Root(models.Model):
    """A lexical root. Used for grouping together related lexemes."""
    helpset = models.ForeignKey(HelpSet, models.CASCADE, related_name="roots")
    text = models.CharField(max_length=100)

    class Meta:
        ordering = ["text"]
        constraints = [
            models.UniqueConstraint(
                fields=["text", "helpset"], 
                name="root_text_unique",
            )
        ]

    def __str__(self) -> str:
        return f"{self.text} ({self.helpset})"


class Lexeme(models.Model):
    """An abstract lexeme."""
    # NOTE: User should be warned when deleting a lexeme 
    # that still has links as they will also be deleted.
    helpset = models.ForeignKey(HelpSet, models.CASCADE, related_name="lexemes")
    text = models.CharField(max_length=100)
    root = models.ForeignKey(Root, models.SET_NULL, null=True, blank=True)
    help_text = models.TextField(null=True, blank=True)
    help_image = models.ImageField(default="", blank=True)

    def __str__(self) -> str:
        return f"{self.text} ({self.helpset})"

    class Meta:
        ordering = ["text"]
        constraints = [
            models.UniqueConstraint(
                fields=["text", "helpset"], 
                name="lexeme_text_unqiue",
            )
        ]


class Link(models.Model):
    """A link between a concrete word form and the lexeme it is derived from.
    Distinct lexemes may have forms that are morphologically identical and
    so multiple links may have the same text but point to different lexemes.
    """
    helpset = models.ForeignKey(HelpSet, models.CASCADE, related_name="links")
    word = models.CharField(max_length=100)
    lexeme = models.ForeignKey(Lexeme, models.CASCADE, related_name="links")
    parse_data = models.CharField(max_length=200, blank=True, default="")

    def __str__(self) -> str:
        return f"{self.word} -> {self.lexeme.text} ({self.helpset})"

    class Meta:
        ordering = ["word"]
        constraints = [
            models.UniqueConstraint(
                fields=["word", "lexeme"],
                name="word_lexeme_pair_unique",
            ),
        ]


class Book(models.Model):
    """A book. Essentially just text but stored in the JSON format 
    for structure."""
    name = models.CharField(max_length=100, unique=True)
    text = models.JSONField()
