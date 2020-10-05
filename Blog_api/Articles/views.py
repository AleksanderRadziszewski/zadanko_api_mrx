from django.shortcuts import render
from django.views import View

from Articles.forms import ArticlesForm
from Articles.models import Articles


class ArticlesView(View):
    def get(self,request):
        form=ArticlesForm()
        return render(request, "Blog/form.html", {"form":form})
    def post(self,request):
        form=ArticlesForm(request.POST)
        if form.is_valid():
            Articles.objects.create(**form.cleaned_data)
        return render(request, "Blog/form.html", {"form":form})

# Create your views here.
