from django import template

register = template.Library()

def is_article_read(article, user):
    return bool(article.alreadyreadarticle_set.filter(user=user))

register.filter('is_article_read', is_article_read)
