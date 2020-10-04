from django.db import models


class Entry(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(null=True)
    modified = models.DateTimeField(null=True)
    pub_date = models.DateTimeField(null=True)
    comments_count = models.IntegerField()
