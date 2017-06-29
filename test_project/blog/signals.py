from django.urls import reverse_lazy
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.contrib.sites.models import Site
from django.conf import  settings

from .models import Subscriptions, Blog, AlreadyReadArticle, Article

@receiver(post_save, sender=User)
def create_blog_for_new_user(sender, created, instance, **kwargs):
    if created:
        new_blog = Blog(name="Blog name", owner=instance)
        new_blog.save()
        new_subscription = Subscriptions(user=instance, blog=new_blog)
        new_subscription.save()

@receiver(post_delete, sender=Subscriptions)
def remove_already_read_article(sender, instance, using, **kwargs):
    AlreadyReadArticle.objects.filter(article__blog=instance.blog, user=instance.user).delete()

@receiver(post_save, sender=Article)
def create_blog_for_new_user(sender, created, instance, **kwargs):
    '''
    This function should be moved to celery task.
    '''
    if created:
        site = Site.objects.get(id=settings.SITE_ID)
        rev_url = reverse_lazy('article_view', kwargs={"pk": instance.id}).__str__()
        for sub in Subscriptions.objects.filter(blog=instance.blog):
            if sub.user.email:
                site_url = ''.join([site.domain, rev_url ])
                try:
                    send_mail(
                        'At blog %s was added new article' % (instance.blog.name),
                        'Here is the link: <a href="%s">%s</a>.' % (site_url , instance.name),
                        'from@example.com',
                        [sub.user.email],
                        fail_silently=False,
                    )
                except Exception as e:
                    print(e)
