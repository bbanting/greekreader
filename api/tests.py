from typing import Any

from django.test import TestCase
from django.db.models import Model
from django.contrib.auth.models import User

from .models import HelpSet, Lexeme, WordLink, Root


def exists(model:Model, pk:Any, pk_field_name:str="pk", manager:str="_default_manager") -> bool:
    """Returns True if an entry with the provided pk exists 
    in the database. False if it doesn't."""
    return bool(getattr(model, manager).filter(**{pk_field_name: pk}))


class HelpSetTestCase(TestCase):
    def setUp(self) -> None:
        user = User.objects.create(username="test", password="pass")
        self.hs = HelpSet.objects.create(name="name", author=user)

    def test_last_modified_updated_on_root_save(self) -> None:
        last_modified = self.hs.last_modified
        Root.objects.create(helpset=self.hs, text="hello")
        self.assertGreater(self.hs.last_modified, last_modified)

    def test_last_modified_updated_on_root_delete(self) -> None:
        root = Root.objects.create(helpset=self.hs, text="hello")
        last_modified = self.hs.last_modified
        root.delete()
        self.assertGreater(self.hs.last_modified, last_modified)

    def test_last_modified_updated_on_lexeme_save(self) -> None:
        last_modified = self.hs.last_modified
        Lexeme.objects.create(helpset=self.hs, text="hello")
        self.assertGreater(self.hs.last_modified, last_modified)

    def test_last_modified_updated_on_lexeme_delete(self) -> None:
        lex = Lexeme.objects.create(helpset=self.hs, text="hello")
        last_modified = self.hs.last_modified
        lex.delete()
        self.assertGreater(self.hs.last_modified, last_modified)
  
    def test_last_modified_updated_on_link_save(self) -> None:
        lex = Lexeme.objects.create(helpset=self.hs, text="hello")
        last_modified = self.hs.last_modified
        WordLink.objects.create(helpset=self.hs, word="hey", lexeme=lex)
        self.assertGreater(self.hs.last_modified, last_modified)

    def test_last_modified_updated_on_link_delete(self) -> None:
        lex = Lexeme.objects.create(helpset=self.hs, text="hello")
        link = WordLink.objects.create(helpset=self.hs, word="hey", lexeme=lex)
        last_modified = self.hs.last_modified
        link.delete()
        self.assertGreater(self.hs.last_modified, last_modified)


