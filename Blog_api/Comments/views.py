from django.shortcuts import render
from django.views import View
from Blog_api.tasks import task


class CommentsView(View):
    def get(self,request):
        task.delay()
        return "Hello"


# Create your views here.
