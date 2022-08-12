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
    helpset = models.ForeignKey(HelpSet, models.CASCADE)
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
    helpset = models.ForeignKey(HelpSet, models.CASCADE, related_name="lexemes")
    text = models.CharField(max_length=100)
    root = models.ForeignKey(Root, models.SET_NULL, null=True, blank=True)
    help_text = models.TextField(null=True, blank=True)
    help_image = models.ImageField(default="", blank=True)
    words = models.ManyToManyField("Word", related_name="lexemes", through="Link")

    class Meta:
        ordering = ["text"]
        constraints = [
            models.UniqueConstraint(
                fields=["text", "helpset"], 
                name="lexeme_text_unqiue",
            )
        ]

    # NOTE: User should be warned when deleting a lexeme 
    # that still has linked words. Words that have no other links
    # should be deleted.
    def delete(self, *args, **kwargs) -> None:
        for word in self.words.all():
            if len(word.lexemes.all()) > 1:
                continue
            word.delete()
        super().delete(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.text} ({self.helpset})"


class Word(models.Model):
    """A concrete manifestation of a lexeme."""
    helpset = models.ForeignKey(HelpSet, models.CASCADE, related_name="words")
    text = models.CharField(max_length=100)

    class Meta:
        ordering = ["text"]
        constraints = [
            models.UniqueConstraint(
                fields=["helpset", "text"], 
                name="word_text_unique",
            )
        ]

    def __str__(self) -> str:
        return f"{self.text} ({self.helpset})"


class Link(models.Model):
    """A link between a word and the lexeme it is derived from.
    Distinct lexemes may have forms that are morphologically identical.
    """
    # TODO: If a link is deleted, delete the word if it has no other links
    lexeme = models.ForeignKey(Lexeme, models.CASCADE, related_name="links")
    word = models.ForeignKey(Word, models.CASCADE, related_name="links")
    parse_data = models.CharField(max_length=200, blank=True, default="")  

    @property
    def helpset(self) -> HelpSet | None:
        """Retrieve the helpset it belongs to."""
        return self.lexeme.helpset

    def __str__(self) -> str:
        return f"{self.word.text} -> {self.lexeme.text} ({self.helpset})"


class Book(models.Model):
    """A book. Essentially just text but stored in the JSON format 
    for structure."""
    name = models.CharField(max_length=100, unique=True)
    text = models.JSONField()
