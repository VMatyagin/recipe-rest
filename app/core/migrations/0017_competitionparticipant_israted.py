# Generated by Django 3.1.12 on 2021-07-02 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0016_auto_20210702_0929"),
    ]

    operations = [
        migrations.AddField(
            model_name="competitionparticipant",
            name="isRated",
            field=models.BooleanField(default=True),
        ),
    ]