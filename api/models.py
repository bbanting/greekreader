from django.db import models
from django.contrib.auth.models import User


class HelpSet(models.Model):
    """A set of lexical helps."""
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) # NOTE: Set when altering Lexeme


class Root(models.Model):
    """A lexical root. Used for grouping together related lexemes."""
    helpset = models.ForeignKey(HelpSet, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)


class Lexeme(models.Model):
    """An abstract lexeme."""
    # NOTE: User should be warned when deleting a lexeme 
    # that still has linked words. Words that have no other links
    # should be deleted.
    helpset = models.ForeignKey(HelpSet, on_delete=models.CASCADE)
    root = models.ForeignKey(Root, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.CharField(max_length=100)
    help_text = models.TextField(null=True, blank=True)
    help_image = models.ImageField()
    words = models.ManyToManyField("Word", related_name="lexemes", through="Link")


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


class Link(models.Model):
    """A link between a word and the lexeme it is derived from.
    Distinct lexemes may have forms that are morphologically identical.
    """
    lexeme = models.ForeignKey(Lexeme, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    parse_data = models.CharField(max_length=200, blank=True, default="")
