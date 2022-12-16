import uuid

from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

from accounts.models import Human


class StudyGroup(models.Model):
    """A group of students with at least one teacher."""
    date_created = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(Human, models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=50)
    users = models.ManyToManyField(Human, through="Membership", blank=True, related_name="studygroups")
    TIER_CHOICES = [(1, "One"), (2, "Two"), (3, "Three")]
    tier = models.IntegerField(choices=TIER_CHOICES, default=1)
    shelf = models.ManyToManyField("Book", blank=True)

    class Meta:
        ordering = ["-tier"]


class Membership(models.Model):
    """A user's membership in a study group. The through model for Profile 
    and StudyGroup.
    """
    studygroup = models.ForeignKey(StudyGroup, models.CASCADE)
    user = models.ForeignKey(Human, models.CASCADE, related_name="memberships")
    is_teacher = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ["user", "studygroup"],
                name = "unique_users_in_studygroup",
            )
        ]


class HelpSet(models.Model):
    """A set of lexical helps."""
    date_created = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(Human, models.SET_NULL, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class HelpSetSettings(models.Model):
    """A model for the settings for a helpset."""
    last_modified = models.DateTimeField(auto_now=True)
    helpset = models.OneToOneField(HelpSet, models.CASCADE, related_name="settings")
    
    parsings_label = models.CharField(max_length=20)


class Root(models.Model):
    """A lexical root. Used for grouping together related lexemes."""
    date_created = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(Human, models.SET_NULL, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    # last_modified_by = models.ForeignKey(Human, models.SET_NULL, null=True)

    helpset = models.ForeignKey(HelpSet, models.CASCADE, related_name="roots")
    text = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"({self.helpset}) {self.text}"

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
    # that still has Words as they will also be deleted.
    date_created = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(Human, models.SET_NULL, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    # last_modified_by = models.ForeignKey(Human, models.SET_NULL, null=True)

    helpset = models.ForeignKey(HelpSet, models.CASCADE, related_name="lexemes")
    text = models.CharField(max_length=100)
    root = models.ForeignKey(Root, models.SET_NULL, null=True, blank=True)
    help_text = models.TextField(null=True, blank=True)
    help_images = models.ManyToManyField("HelpImage", blank=True)

    def __str__(self) -> str:
        return f"({self.helpset}) {self.text}"

    class Meta:
        ordering = ["text"]


def name_image_file(instance, filename) -> str:
    extension = filename[filename.rfind("."):]
    return f"images/{uuid.uuid4()}{extension}"

class HelpImage(models.Model):
    """An image to be used as a vocabulary help. May be linked to
    multiple lexemes.
    """
    date_created = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(Human, models.SET_NULL, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    # last_modified_by = models.ForeignKey(Human, models.SET_NULL, null=True)

    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to=name_image_file)

    def __str__(self) -> str:
        return f"{self.title:.20}"


class Word(models.Model):
    """A link between a concrete word form and the lexeme it is derived from.
    Distinct lexemes may have forms that are morphologically identical and
    so multiple Words may have the same text but point to different lexemes.
    """
    date_created = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(Human, models.SET_NULL, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    # last_modified_by = models.ForeignKey(Human, models.SET_NULL, null=True)

    helpset = models.ForeignKey(HelpSet, models.CASCADE, related_name="words")
    text = models.CharField(max_length=100)
    lexeme = models.ForeignKey(Lexeme, models.CASCADE, related_name="words")
    order = models.IntegerField(blank=True, default=0)
    # parsings 

    def __str__(self) -> str:
        return f"({self.helpset}) {self.text} -> {self.lexeme.text}"

    class Meta:
        ordering = ["text", "order"]
        constraints = [
            models.UniqueConstraint(
                fields=["text", "lexeme"],
                name="word_lexeme_pair_unique",
            ),
        ]


class Parsing(models.Model):
    """A parsing of a particular word form."""
    date_created = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(Human, models.SET_NULL, null=True)
    last_modified = models.DateTimeField(auto_now=True)

    word = models.ForeignKey(Word, models.CASCADE, related_name="parsings")
    content = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"({self.word}) {self.content}"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["word", "content"],
                name="parsing_unique_for_word",
            )
        ]


# NOTE: There should be a limit of how many collections a user can make
class Collection(models.Model):
    """An arbitrary grouping of books by the user."""
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    study_group = models.ForeignKey(Human, models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    books = models.ManyToManyField("Book")


class Book(models.Model):
    """A book, divided into chapters."""
    date_created = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(Human, models.SET_NULL, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    # last_modified_by = models.ForeignKey(Human, models.SET_NULL, null=True)

    name = models.CharField(max_length=100, unique=True)
    cover_image = models.ForeignKey(HelpImage, models.SET_NULL, blank=True, null=True)
    helpset = models.ForeignKey(HelpSet, models.SET_NULL, blank=True, null=True, related_name="books")
    fallback_helpset = models.ForeignKey(HelpSet, models.SET_NULL, blank=True, null=True, related_name="fallback_books")
    TIER_CHOICES = [(1, "One"), (2, "Two"), (3, "Three")]
    tier = models.IntegerField(choices=TIER_CHOICES, default=1)

    def __str__(self) -> str:
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["helpset", "fallback_helpset"],
                name="helpset_not_same_as_fallback",
            )
        ]


def not_negative(value:int) -> None:
    """Check if a number value is negative."""
    if value < 0:
        raise ValidationError(
            "The number may not be negative", 
            params={"value": value}
            )


class Chapter(models.Model):
    """A chapter in a book."""
    date_created = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(Human, models.SET_NULL, null=True)
    last_modified = models.DateTimeField(auto_now=True)

    book = models.ForeignKey(Book, models.CASCADE, related_name="chapters")
    order = models.IntegerField(validators=[not_negative])
    ordinal_text = models.CharField(max_length=50)
    title = models.CharField(max_length=100, blank=True, default="")
    content = models.TextField(blank=True, default="")

    def __str__(self) -> str:
        return f"{self.book.name}: {self.ordinal_text} ({self.order})"

    class Meta:
        ordering = ["order"]
        constraints = [
            models.UniqueConstraint(
                fields=["book", "order"],
                name="chapter_order_unique",
            ),
        ]
