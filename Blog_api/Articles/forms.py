from django import forms
from Articles.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields="__all__"