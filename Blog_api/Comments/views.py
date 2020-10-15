from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .forms import AddCommentForm
from Blog_api.tasks import task
from Comments.models import Comments


class CommentsListView(ListView):
    model = Comments
    template_name = "Comments/comments_list.html"


class CommentsAddView(View):
    def get(self, request, article_id):
        form = AddCommentForm()
        return render(request, "Comments/add_comment.html", {"form": form})

    def post(self, request, article_id):
        form = AddCommentForm(request.POST)
        if form.is_valid():
            Comments.objects.create(**form.cleaned_data)
            task.delay(article_id)
        return render(request, "Comments/add_comment.html", {"form": form})


# Create your views here.
