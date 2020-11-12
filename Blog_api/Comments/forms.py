from django import forms
from comments.models import Comments


class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = "__all__"
