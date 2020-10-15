from django import forms
from Comments.models import Comments


class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = "__all__"
