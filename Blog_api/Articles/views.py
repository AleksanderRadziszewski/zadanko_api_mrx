from django.shortcuts import render
from django.views import View

from Articles.forms import ArticleForm
from Articles.models import Article


class ArticlesView(View):
    def get(self,request):
        form=ArticleForm()
        return render(request, "Blog/form.html", {"form":form})
    def post(self,request):
        form=ArticleForm(request.POST)
        if form.is_valid():
            Article.objects.create(**form.cleaned_data)
        return render(request, "Blog/form.html", {"form":form})

# Create your views here.
