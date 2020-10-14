from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView,LogoutView
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView
from django.db import models
from Blog.forms import EntryForm
from Blog.models import Entry
from django.contrib.auth.signals import user_logged_in
from Products.forms import CreateProfileForm


class LoginBlogView(LoginView):
    template_name = "Blog/login.html"

class LogOutView(LogoutView):
    next_page = "/"

class Profile(models.Model):
    phone_number = models.CharField(max_length=40)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adress = models.TextField()

class CreateProfileView(FormView):
    form_class = CreateProfileForm
    template_name = "Products/create_profile.html"
    success_url = "/"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        Profile.objects.create(user=user, phone_number=form.cleaned_data["phone_number"],
                               adress=form.cleaned_data["adress"])
        return super().form_valid(form)


def create_profile(sender, user, request, **kwargs):
    Profile.objects.get_or_create(user=user)


user_logged_in.connect(create_profile)


class EntryView(View):
    def get(self, request):
        form = EntryForm()
        return render(request, "Blog/form.html", {"form": form})

    def post(self, request):
        form = EntryForm(request.POST)
        if form.is_valid():
            Entry.objects.create(**form.cleaned_data)
        return render(request, "Blog/form.html", {"form": form})




# Create your views here.
