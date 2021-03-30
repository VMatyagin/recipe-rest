# Generated by Django 3.1.7 on 2021-03-06 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210305_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='worth',
            field=models.IntegerField(choices=[(0, 'Не учитывается'), (1, 'Творчество'), (2, 'Спорт'), (3, 'Волонтерство'), (4, 'Городское')], default=0, verbose_name='Ценность блоков'),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.IntegerField(choices=[(0, 'Мероприятие создано'), (1, 'Мероприятие прошло'), (2, 'Мероприятие не прошло')], default=0, verbose_name='Статус мероприятия'),
        ),
    ]