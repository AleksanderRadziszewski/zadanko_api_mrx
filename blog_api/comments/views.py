from comments.models import Comments
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from blog_api.tasks import task

from .forms import AddCommentForm


class CommentsListView(ListView):
    model = Comments
    template_name = "object_list.html"

    def get_queryset(self):
        return Comments.objects.filter(body__isnull=False)


class CommentsAddView(View):
    def get(self, request):
        form = AddCommentForm()
        return render(request, "comments/add_comment.html", {"form": form})

    def post(self, request, article_id):
        form = AddCommentForm(request.POST)
        if form.is_valid():
            Comments.objects.create(**form.cleaned_data)
            task.delay(article_id)
        return redirect(reverse("articles list"))

