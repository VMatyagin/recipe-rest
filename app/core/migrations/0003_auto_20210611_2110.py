# Generated by Django 3.1.12 on 2021-06-11 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0002_auto_20210611_2045")]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="startDate",
            field=models.DateTimeField(verbose_name="Дата начала"),
        )
    ]
