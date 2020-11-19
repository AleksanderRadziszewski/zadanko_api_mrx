from __future__ import absolute_import
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_api.settings')


# app = Celery('blog_api', backend='amqp://', include=['blog_api.tasks'])

app = Celery('blog_api',
             broker='amqp://guest@localhost//',
             backend='amqp://',
             include=['blog_api.tasks'])


app.conf.broker_url = 'redis://localhost:6379/0'
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.result_backend = 'redis://localhost:6379/0'


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


if __name__ == '__main__':
    app.start()
