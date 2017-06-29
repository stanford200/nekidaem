from .forms import ArticleForm

class ArticleAbstract(object):
    template_name = 'blog/article_add.html'
    success_url = '/'
    form_class = ArticleForm

    def get_form_kwargs(self):
        kwargs = super(ArticleAbstract, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        result = super(ArticleAbstract, self).form_valid(form)
        return result