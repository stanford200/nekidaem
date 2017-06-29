from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .views import CreateArticleView, UpdateArticleView, DeleteArticleView, ArtticleDetailView,\
    BlogListView, ArticleListView, subscribe, unsubscribe, NewsListView


urlpatterns = [
    url(r'^blog/(?P<pk>\d+)/subscribe$', login_required(subscribe), name='subscribe'),
    url(r'^blog/(?P<pk>\d+)/unsubscribe$', login_required(unsubscribe), name='unsubscribe'),

    url(r'^blog/(?P<pk>\d+)/articles$', ArticleListView.as_view(), name='blog_view'),
    url(r'^blogs/$', BlogListView.as_view(), name='blogs'),

    url(r'^article/(?P<pk>\d+)/edit', login_required(UpdateArticleView.as_view(), '/accounts/login'), name='article_edit'),
    url(r'^article/(?P<pk>\d+)/delete', login_required(DeleteArticleView.as_view(), '/accounts/login'), name='article_delete'),
    url(r'^article/(?P<pk>\d+)/view', ArtticleDetailView.as_view(), name='article_view'),
    url(r'^article/', login_required(CreateArticleView.as_view(), '/accounts/login'), name='article_create'),

    url(r'^news/$', login_required(NewsListView.as_view(), '/account/login'), name='news'),

    url(r'^$', login_required(ArticleListView.as_view(), '/accounts/login'), name='own_blog'),
]
