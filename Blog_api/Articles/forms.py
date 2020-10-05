from django import forms
from Articles.models import Articles


class ArticlesForm(forms.ModelForm):
    class Meta:
        model=Articles
        fields="__all__"