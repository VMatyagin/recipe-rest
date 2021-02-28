# Generated by Django 3.1.7 on 2021-02-28 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='boec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='seasons', to='core.boec', verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='season',
            name='brigade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.brigade', verbose_name='Отряд'),
        ),
        migrations.AlterField(
            model_name='season',
            name='year',
            field=models.IntegerField(verbose_name='Год выезда'),
        ),
    ]