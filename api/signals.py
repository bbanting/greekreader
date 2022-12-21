"""Signals registered here. Imported in the app config."""
from django.db.models.signals import post_save, post_delete
from django.utils import timezone
from django.dispatch import receiver

from .models import Root, Lexeme, WordLink


@receiver((post_save, post_delete), sender=Root)
@receiver((post_save, post_delete), sender=Lexeme)
@receiver((post_save, post_delete), sender=WordLink)
def helpset_update_last_modified(sender, **kwargs) -> None:
    """Update the last_modified attribute of the HelpSet. This may be
    replaced by custom save() and delete() methods in the future
    but for now this workds and is less verbose."""
    instance = kwargs.get("instance")
    instance.helpset.last_modified = timezone.now()
    instance.helpset.save()
