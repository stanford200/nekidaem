from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from .models import Subscriptions, Blog

@receiver(post_save, sender=User)
def create_blog_for_new_user(sender, created, instance, **kwargs):
    if created:
        new_blog = Blog(name="Blog name", owner=instance)
        new_blog.save()
        new_subscription = Subscriptions(user=instance, blog=new_blog)
        new_subscription.save()
