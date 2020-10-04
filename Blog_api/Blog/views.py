from django.shortcuts import render

from django.http import request
from django.shortcuts import render
from django.views import View

from Blog.forms import EntryForm
from Blog.models import Entry


class EntryView(View):
    def get(self,request):
        form=EntryForm()
        return render(request,"Blog/form.html", {"form":form})
    def post(self,request):
        form=EntryForm(request.POST)
        if form.is_valid():
            Entry.objects.create(**form.cleaned_data)
        return render(request,"Blog/form.html", {"form":form})
# Create your views here.
