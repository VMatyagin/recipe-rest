# Generated by Django 3.1.5 on 2021-01-07 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_brigade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brigade',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.area'),
        ),
        migrations.AlterField(
            model_name='brigade',
            name='shtab',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.shtab'),
        ),
    ]
