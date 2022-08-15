from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class HelpSet(models.Model):
    """A set of lexical helps."""
    date_created = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, models.SET_NULL, null=True)
    last_modified = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        # This ordering is for the sake of Book easily resolving helpset order
        ordering = ["bookhelpsetinstance__order"]


class Root(models.Model):
    """A lexical root. Used for grouping together related lexemes."""
    date_created = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, models.SET_NULL, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, models.SET_NULL, null=True)

    helpset = models.ForeignKey(HelpSet, models.CASCADE, related_name="roots")
    text = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.text} ({self.helpset})"

    class Meta:
        ordering = ["text"]
        constraints = [
            models.UniqueConstraint(
                fields=["text", "helpset"], 
                name="root_text_unique",
            )
        ]


class Lexeme(models.Model):
    """An abstract lexeme."""
    # NOTE: User should be warned when deleting a lexeme 
    # that still has links as they will also be deleted.
    date_created = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, models.SET_NULL, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, models.SET_NULL, null=True)

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
    date_created = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, models.SET_NULL, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, models.SET_NULL, null=True)

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


class BookHelpSetInstance(models.Model):
    """Through table for Book and HelpSet to enable ordering."""
    book = models.ForeignKey("Book", models.CASCADE)
    helpset = models.ForeignKey(HelpSet, models.CASCADE)
    order = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.book} -> {self.helpset.name} ({self.order})"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["book", "helpset"],
                name="book_helpset_unique",
            ),
        ]


class Book(models.Model):
    """A book. Essentially just text but stored in the JSON format 
    for use by the JS frontend."""
    date_created = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, models.SET_NULL, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, models.SET_NULL, null=True)

    name = models.CharField(max_length=100, unique=True)
    text = models.JSONField()
    helpsets = models.ManyToManyField(HelpSet, through=BookHelpSetInstance, blank=True)

    def __str__(self) -> str:
        return self.name
