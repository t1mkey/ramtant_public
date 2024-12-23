from django.db.models.signals import post_save
from django.contrib.auth.models import User

from django.dispatch import receiver

from django.core.exceptions import ObjectDoesNotExist

from .models import Profile, Usr

@receiver(post_save, sender=Usr)
def create_prf(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Usr)
def save_prf(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)
 