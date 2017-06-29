from django import template

register = template.Library()

def is_subscribed(blog, user):
    return bool(blog.subscriptions_set.filter(user=user))

register.filter('is_subscribed', is_subscribed)
