from datetime import date

from django.utils import timezone
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100,unique=True)
    body = models.TextField()
    created = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    modified = models.DateTimeField(null=True, auto_now=True)
    pub_date = models.DateTimeField(null=True, default=date.today())
    comments_count = models.IntegerField(default=0)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Article"
        verbose_name_plural="Articles"
