from __future__ import absolute_import
import os
from django.core.mail import send_mail
from articles.models import Article
from .celery import app
from comments.models import Comments

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_api.settings')

@app.task
def task(article_id):
    article = Article.objects.get(pk=article_id)
    comments_amount = Comments.objects.filter(article=article).count()
    article.comments_count = comments_amount
    article.save()


@app.task
def email_task(total_price, email):
    send_mail(
        "Total price of your purchases",
        f"Total price of your purchases is {total_price} zł",
        "xxx@gmail.com",
        [f"{email}"],
        fail_silently=False)
