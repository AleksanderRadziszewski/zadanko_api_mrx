from django import forms
from django.contrib.auth.models import User

from Comments.models import Comments


class AddCommentForm(forms.ModelForm):

    class Meta:
        model=Comments
        fields="__all__"
