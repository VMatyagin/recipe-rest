# Generated by Django 3.1.12 on 2021-06-17 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210617_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='isCanonical',
            field=models.BooleanField(default=False, verbose_name='Каноничность'),
        ),
    ]