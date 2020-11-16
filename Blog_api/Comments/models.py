from django.db import models
from blog.models import Entry
from articles.models import Article


class Comments(models.Model):
    body = models.TextField()
    created = models.DateTimeField(null=True, auto_now=True)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, default=0)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default=0)

    class Meta:
        verbose_name="Comment"
        verbose_name_plural="comments"
