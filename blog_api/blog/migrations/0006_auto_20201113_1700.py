# Generated by Django 3.1.2 on 2020-11-13 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201113_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
