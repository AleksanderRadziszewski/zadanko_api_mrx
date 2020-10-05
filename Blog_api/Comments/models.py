from django.db import models
from Blog.models import Entry
from Articles.models import Article

class Comments(models.Model):
    body = models.TextField()
    created = models.DateTimeField(null=True,auto_now=True)
    entry=models.ForeignKey(Entry,on_delete=models.CASCADE,default=0)
    article=models.ForeignKey(Article,on_delete=models.CASCADE,default=0)
# Create your models here.
