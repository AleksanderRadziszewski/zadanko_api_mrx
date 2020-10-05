from django.db import models

class Comments(models.Model):
    body = models.TextField()
    created = models.DateTimeField(null=True,auto_now=True)

# Create your models here.
