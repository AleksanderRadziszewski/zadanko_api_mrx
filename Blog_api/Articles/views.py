from datetime import date

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DeleteView, DetailView, CreateView
from articles.documents import ArticleDocument
from articles.forms import ArticleForm, ArticleSearchForm
from articles.models import Article


class ArticlesListView(ListView):
    model = Article
    template_name = "object_list.html"

    def get_queryset(self):
        return Article.objects.filter(pub_date__isnull=False)


class ArticleDetailView(DetailView):
    pk_url_kwarg = "article_id"
    template_name = "articles/article_detail.html"
    queryset = Article.objects.all()

    def get_object(self, queryset=None):
            article_id=self.kwargs.get(self.pk_url_kwarg)
            for article in self.queryset:
                if article_id!=article.id:
                    raise AttributeError(
                         f"No article with id {article_id}"
                                 )
                obj=self.queryset.get()
                return obj


class ArticleAddView(CreateView):
    form_class = ArticleForm
    success_url = reverse_lazy("articles list")
    template_name = "Articles/form.html"


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("articles list")


class ArticleSearchView(View):
    def get(self, request):
        form=ArticleSearchForm()
        return render(request, "articles/autocomplete.html", {"form":form})

    def post(self, request):
        form=ArticleSearchForm(request.POST)
        if form.is_valid():
            s = ArticleDocument.search().query("match_phrase_prefix", title=form.cleaned_data.get("search"))
            qs = s.to_queryset()
            if qs:
                titles = []
                for x in qs:
                    titles.append(x.title)
            else:
                raise ValueError(f"No phrase with {form.cleaned_data.get('search')}")

        else:
            raise ValueError(f"Typing value{form.cleaned_data.get('search')} isn't correct ")
        return render(request, "articles/autocomplete.html", {"form":form,
                                                              "titles": titles})


