from django.contrib import admin

from .models import Blog, Article, Subscriptions

# Register your models here.

admin.site.register(Blog)
admin.site.register(Article)
admin.site.register(Subscriptions)
