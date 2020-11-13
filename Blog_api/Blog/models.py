from datetime import date
from django.contrib.auth.models import User
from django.db import models


class Entry(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    created = models.DateTimeField(null=True, auto_now_add=True)
    modified = models.DateTimeField(null=True, auto_now=True)
    pub_date = models.DateTimeField(null=True,blank=True)
    comments_count = models.IntegerField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Entry"
        verbose_name_plural="Entries"

class Profile(models.Model):
    phone_number = models.CharField(max_length=40)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adress = models.TextField()

    class Meta:
        verbose_name="Profile"
        verbose_name_plural="Profiles"
