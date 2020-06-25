from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import *

@receiver(post_save, sender=User)
def build_profile_on_user_creation(sender, instance, created, **kwargs):
    print("in signals")
    if created:
        print(sender, 'This is sender')
        print(instance, 'This is instance')
        profile = Profile(user=instance)
        profile.save()

