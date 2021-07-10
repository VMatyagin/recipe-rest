# Generated by Django 3.1.12 on 2021-07-02 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0017_competitionparticipant_israted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="competitionparticipant",
            name="worth",
            field=models.IntegerField(
                choices=[(0, "Заявка"), (1, "Участие/плей-офф")],
                default=0,
                verbose_name="Статус участника",
            ),
        ),
        migrations.AlterField(
            model_name="nomination",
            name="owner",
            field=models.ManyToManyField(
                blank=True, related_name="nomination", to="core.CompetitionParticipant"
            ),
        ),
    ]
