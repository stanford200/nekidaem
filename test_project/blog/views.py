from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView

from .models import Article, Blog, Subscriptions
from .helpers import ArticleAbstract

# Create your views here.


class CreateArticleView(ArticleAbstract, CreateView):
    template_name = 'blog/article_add.html'


class UpdateArticleView(ArticleAbstract, UpdateView):
    template_name = 'blog/article_update.html'
    model = Article


class DeleteArticleView(DeleteView):
    model = Article
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ArtticleDetailView(DetailView):
    model = Article


class BlogListView(ListView):
    model = Blog


class ArticleListView(ListView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        if self.kwargs.get('pk'):
            try:
                blog = Blog.objects.get(id=self.kwargs.get('pk'))
                context['is_owner'] = blog.owner == self.request.user
            except Blog.DoesNotExist:
                context['is_owner'] = False
        return context

    def get_queryset(self):
        queryset = super(ArticleListView, self).get_queryset()
        if self.kwargs.get('pk'):
            return queryset.filter(blog_id=self.kwargs.get('pk'))
        elif not self.request.user.is_anonymous:
            return queryset.filter(blog__owner=self.request.user)
        return queryset

def subscribe(request, pk):
    new_subscription = Subscriptions(blog_id=pk, user=request.user)
    try:
        new_subscription.save()
    except Exception:
        pass
    return HttpResponseRedirect(reverse('blog_view', kwargs={'pk': pk}))

def unsubscribe(request, pk):
    Subscriptions.objects.filter(blog_id=pk, user=request.user).delete()
    return HttpResponseRedirect(reverse('blog_view', kwargs={'pk': pk}))
