# Generated by Django 2.2.6 on 2020-10-05 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201005_1255'),
        ('articles', '0002_auto_20201005_1255'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='article',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='articles.Article'),
        ),
        migrations.AddField(
            model_name='comments',
            name='entry',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.Entry'),
        ),
    ]