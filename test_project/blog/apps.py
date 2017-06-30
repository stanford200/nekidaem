from django.apps import AppConfig

class ActivityBlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        from blog import signals
