from celery.app import task
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections,Search

from Articles.documents import ArticleDocument
from Articles.forms import ArticleForm
from Articles.models import Article
from Comments.models import Comments
from Blog_api.tasks import task


class ArticlesListView(ListView):
    model=Article
    paginate_by = 2
    template_name = "Articles/article_list.html"

class ArticleDetailView(View):

    def get(self,request,article_id):
        article = Article.objects.get(pk=article_id)

        return render(request, "Articles/article_detail.html", {"article": article})


class ArticlesAddView(View):
    def get(self,request):
        form=ArticleForm()
        return render(request,"Articles/form.html",{"form":form})
    def post(self,request):
        form=ArticleForm(request.POST)
        if form.is_valid():
            Article.objects.create(**form.cleaned_data)
        return redirect("/articles_list/")


class SearchView(View):
    def get(self, request):
        return render(request, "articles/autocomplete.html")

    def post(self, request):
        s = ArticleDocument.search().query("match_phrase_prefix", title=request.POST.get("article_search"))
        qs = s.to_queryset()
        titles = list()
        for x in qs:
            if x is not None:
                titles.append(x.title)
                print(titles)
            else:
                pass
        return render(request, "articles/article_api.html",{"titles":titles})

# Create your views here.
