from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver([post_save, post_delete])
def clear_cache(sender, instance, **kwargs):
    cache.clear()