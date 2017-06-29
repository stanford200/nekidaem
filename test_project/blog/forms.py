from django import forms

from .models import Article, Blog

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['blog'].queryset = Blog.objects.filter(owner=request.user)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
