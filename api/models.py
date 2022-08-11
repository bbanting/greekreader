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

    def __str__(self) -> str:
        return f"{self.text} ({self.helpset})"


class Lexeme(models.Model):
    """An abstract lexeme."""
    # NOTE: User should be warned when deleting a lexeme 
    # that still has linked words. Words that have no other links
    # should be deleted.
    helpset = models.ForeignKey(HelpSet, models.CASCADE, related_name="lexemes")
    root = models.ForeignKey(Root, models.SET_NULL, null=True, blank=True)
    text = models.CharField(max_length=100)
    help_text = models.TextField(null=True, blank=True)
    help_image = models.ImageField(default="", blank=True)
    words = models.ManyToManyField("Word", related_name="lexemes", through="Link")

    class Meta:
        ordering = ["text"]

    def __str__(self) -> str:
        return f"{self.text} ({self.helpset})"


class Word(models.Model):
    """A concrete manifestation of a lexeme."""
    text = models.CharField(max_length=100)

    @property
    def helpset(self) -> HelpSet | None:
        """Retrieve the helpset it belongs to."""
        try:
            lex = self.lexemes.get()
        except self.DoesNotExist:
            pass
        else:
            return lex.helpset
        return None

    class Meta:
        ordering = ["text"]

    def __str__(self) -> str:
        return f"{self.text} ({self.helpset})"


class Link(models.Model):
    """A link between a word and the lexeme it is derived from.
    Distinct lexemes may have forms that are morphologically identical.
    """
    lexeme = models.ForeignKey(Lexeme, models.CASCADE)
    word = models.ForeignKey(Word, models.CASCADE)
    parse_data = models.CharField(max_length=200, blank=True, default="")  

    def __str__(self) -> str:
        return f"{self.word.text} -> {self.lexeme.text} ({self.lexeme.helpset})"
