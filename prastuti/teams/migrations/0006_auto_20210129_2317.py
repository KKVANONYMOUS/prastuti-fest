# Generated by Django 3.1.5 on 2021-01-29 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20210129_1042'),
        ('teams', '0005_auto_20210129_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.event'),
        ),
    ]
