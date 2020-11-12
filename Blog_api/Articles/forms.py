from django import forms
from articles.models import Article

class ArticleSearchForm(forms.Form):
    search=forms.CharField(max_length=50)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "body", "pub_date"]
