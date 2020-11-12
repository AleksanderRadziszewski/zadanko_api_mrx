# Generated by Django 2.2.6 on 2020-10-05 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('comments_count', models.IntegerField()),
            ],
        ),
    ]
