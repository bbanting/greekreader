from typing import Any

from django.test import TestCase
from django.db.models import Model
from django.contrib.auth.models import User

from .models import HelpSet, Lexeme, Word


def exists(model:Model, pk:Any, pk_field_name:str="pk", manager:str="_default_manager") -> bool:
    """Returns True if an entry with the provided pk exists 
    in the database. False if it doesn't."""
    return bool(getattr(model, manager).filter(**{pk_field_name: pk}))


class LexemeTestCase(TestCase):
    def setUp(self) -> None:
        user = User.objects.create(username="user", password="badpassword")
        self.hs = HelpSet.objects.create(name="hs", author=user)

    def test_delete_side_effect_lonely_words_are_deleted_single(self) -> None:
        lex = Lexeme.objects.create(helpset=self.hs, text="hello")
        word1 = Word.objects.create(helpset=self.hs, text="word1")
        lex.words.add(word1)
        lex.delete()

        self.assertEqual(exists(Word, word1.pk), False)

    def test_delete_side_effect_lonely_words_are_deleted_multiple(self) -> None:
        lex = Lexeme.objects.create(helpset=self.hs, text="hello")
        word1 = Word.objects.create(helpset=self.hs, text="word1")
        word2 = Word.objects.create(helpset=self.hs, text="word2")
        lex.words.add(word1, word2)
        lex.delete()

        self.assertEqual(exists(Word, word1.pk), False)
        self.assertEqual(exists(Word, word2.pk), False)
        
    def test_delete_side_effect_valid_word_not_deleted(self) -> None:
        lex1 = Lexeme.objects.create(helpset=self.hs, text="hello")
        lex2 = Lexeme.objects.create(helpset=self.hs, text="goodbye")
        word1 = Word.objects.create(helpset=self.hs, text="word1")
        word2 = Word.objects.create(helpset=self.hs, text="word2")
        lex1.words.add(word1, word2)
        lex2.words.add(word2)
        lex1.delete()

        self.assertEqual(exists(Word, word1.pk), False)
        self.assertEqual(exists(Word, word2.pk), True)
