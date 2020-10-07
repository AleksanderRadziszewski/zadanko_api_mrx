
from .celery import app

from Comments.models import Comments

@app.task
def task():
    comments_amount=Comments.objects.all().count()
    return comments_amount