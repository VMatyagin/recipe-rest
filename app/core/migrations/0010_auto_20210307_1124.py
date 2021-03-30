# Generated by Django 3.1.7 on 2021-03-07 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210307_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventorder',
            name='place',
            field=models.CharField(blank=True, choices=[(1, 'Первое место'), (2, 'Второе место'), (3, 'Третье место')], max_length=5, null=True, verbose_name='Занятое место'),
        ),
    ]