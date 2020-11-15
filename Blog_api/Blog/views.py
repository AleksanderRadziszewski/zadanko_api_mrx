from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView
from blog.forms import EntryForm
from blog.models import Entry, Profile
from django.contrib.auth.signals import user_logged_in
from products.forms import CreateProfileForm

class CreateProfileView(CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = "Products/create_profile.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        Profile.objects.create(user=user, phone_number=form.cleaned_data["phone_number"],
                               adress=form.cleaned_data["adress"])
        return super().form_valid(form)


def create_profile(user, request, **kwargs):
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
        return redirect("/entry_list/")


class EntryListView(ListView):
    model = Entry
    template_name = "object_list.html"

    def get_queryset(self):
        return Entry.objects.filter(pub_date__isnull=False)


