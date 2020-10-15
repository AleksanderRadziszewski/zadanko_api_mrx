from django.db import models


class Entry(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(null=True, auto_now=True)
    modified = models.DateTimeField(null=True, auto_now=True)
    pub_date = models.DateTimeField(null=True, auto_now_add=True)
    comments_count = models.IntegerField(null=True)

    def __str__(self):
        return self.title
