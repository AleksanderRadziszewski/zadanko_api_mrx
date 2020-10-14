from django import forms
from Articles.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        exclude=["comments_count"]