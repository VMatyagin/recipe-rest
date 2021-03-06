# Generated by Django 3.1.12 on 2021-06-29 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_event_iscanonical"),
    ]

    operations = [
        migrations.AddField(
            model_name="competitionparticipant",
            name="title",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="nomination",
            name="owner",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="nomination",
                to="core.CompetitionParticipant",
            ),
        ),
    ]
