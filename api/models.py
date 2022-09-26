import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class StudyGroup(models.Model):
    """A group of students with at least one 'teacher'."""
    date_created = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, models.SET_NULL, null=True)
    last_modified = models.DateTimeField(auto_now=True)

    lead = models.ForeignKey(User, models.SET_NULL)
    users = models.ManyToManyField(User, through="Membership", blank=True)


class Membership(models.Model):
    """A user's membership in a study group. The through model for Profile 
    and StudyGroup.
    """
    studygroup = models.ForeignKey(StudyGroup, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    is_teacher = models.BooleanField(default=False)


class HelpSet(models.Model):
    """A set of lexical helps."""
    date_created = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, models.SET_NULL, null=True)
    last_modified = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        # This ordering is for the sake of Book resolving helpset order
        ordering = ["helpsetassignment__order"]


class Root(models.Model):
    """A lexical root. Used for grouping together related lexemes."""
    date_created = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, models.SET_NULL, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    # last_modified_by = models.ForeignKey(User, models.SET_NULL, null=True)

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
    # that still has Words as they will also be deleted.
    date_created = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, models.SET_NULL, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    # last_modified_by = models.ForeignKey(User, models.SET_NULL, null=True)

    helpset = models.ForeignKey(HelpSet, models.CASCADE, related_name="lexemes")
    text = models.CharField(max_length=100)
    root = models.ForeignKey(Root, models.SET_NULL, null=True, blank=True)
    help_text = models.TextField(null=True, blank=True)
    help_images = models.ManyToManyField("HelpImage", blank=True)

    def __str__(self) -> str:
        return f"{self.text} ({self.helpset})"

    class Meta:
        ordering = ["text"]


def name_image_file(instance, filename) -> str:
    extension = filename[filename.rfind("."):]
    return f"images/{uuid.uuid4()}{extension}"

class HelpImage(models.Model):
    """An image to be used as a vocabulary help. May be linked to
    multiple lexemes.
    """
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to=name_image_file)


class Word(models.Model):
    """A link between a concrete word form and the lexeme it is derived from.
    Distinct lexemes may have forms that are morphologically identical and
    so multiple Words may have the same text but point to different lexemes.
    """
    date_created = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, models.SET_NULL, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    # last_modified_by = models.ForeignKey(User, models.SET_NULL, null=True)

    helpset = models.ForeignKey(HelpSet, models.CASCADE, related_name="words")
    text = models.CharField(max_length=100)
    lexeme = models.ForeignKey(Lexeme, models.CASCADE, related_name="words")
    parse_data = models.CharField(max_length=200, blank=True, default="")

    def __str__(self) -> str:
        return f"{self.text} -> {self.lexeme.text} ({self.helpset})"

    class Meta:
        ordering = ["text"]
        constraints = [
            models.UniqueConstraint(
                fields=["text", "lexeme"],
                name="word_lexeme_pair_unique",
            ),
        ]


# NOTE: There should be a limit of how many collections a user can make
class Collection(models.Model):
    """An arbitrary grouping of books by the user."""
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    books = models.ManyToManyField("BookAccess")


class HelpSetAssignment(models.Model):
    """Through table for Book and HelpSet to enable ordering. A helpset is
    assigned to a book to enable vocabulary help. If a book has multiple
    helpsets assigned to it, helpsets are accessed in order when a word is
    looked up. For instance, if you have a text that generally aligns with
    Koine Greek but with a few exceptions, you can make another helpset
    and order it higher so to override the default Koine definition."""
    book = models.ForeignKey("Book", models.CASCADE)
    helpset = models.ForeignKey(HelpSet, models.CASCADE)
    order = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.helpset.name} -> {self.book} ({self.order})"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["book", "helpset"],
                name="book_helpset_unique",
            ),
        ]


class Book(models.Model):
    """A book, divided into chapters."""
    date_created = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, models.SET_NULL, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    # last_modified_by = models.ForeignKey(User, models.SET_NULL, null=True)

    name = models.CharField(max_length=100, unique=True)
    cover_image = models.ForeignKey(HelpImage, models.SET_NULL, blank=True, null=True)
    helpsets = models.ManyToManyField(HelpSet, through=HelpSetAssignment, blank=True)

    def __str__(self) -> str:
        return self.name


class Chapter(models.Model):
    """A chapter in a book."""
    book = models.ForeignKey(Book, models.CASCADE, related_name="chapters")
    order = models.IntegerField()
    ordinal_text = models.CharField(max_length=50)
    heading = models.CharField(max_length=100, blank=True, default="")
    content = models.JSONField(blank=True, null=True)

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


class BookPurchase(models.Model):
    """Record of a teacher's purchase of a book."""
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    teacher = models.ForeignKey(User, models.CASCADE)
    book = models.ForeignKey(Book, models.CASCADE)


class BookAccess(models.Model):
    """Access to a book, granted to a student by a teacher."""
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    teacher = models.ForeignKey(User, models.CASCADE, related_name="books_granted")
    student = models.ForeignKey(User, models.CASCADE, related_name="books_received")
    book = models.ForeignKey(BookPurchase, models.CASCADE)
    chapters = models.ManyToManyField(Chapter)
        