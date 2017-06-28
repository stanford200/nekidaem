from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):

    owner = models.ForeignKey(User)

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()

    creation_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog)

    def __str__(self):
        return self.name


class Subscriptions(models.Model):
    """
    We can remove this model and extend 'User' model with m2m on 'Blog',
    but for this project it's more simply to do in such way
    """

    class Meta:
        unique_together = (("user", "blog"),)

    user = models.ForeignKey(User)
    blog= models.ForeignKey(Blog)

    def __str__(self):
        return ' - '.join([self.user.email or self.user.username, self.blog.name])

from .signals import create_blog_for_new_user
