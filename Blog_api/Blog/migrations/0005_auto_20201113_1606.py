# Generated by Django 3.1.2 on 2020-11-13 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name': 'Entry', 'verbose_name_plural': 'Entries'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
        migrations.AlterField(
            model_name='entry',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]