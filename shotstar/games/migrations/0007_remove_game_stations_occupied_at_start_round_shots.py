# Generated by Django 4.0.3 on 2022-03-04 08:33

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_alter_round_game_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='stations_occupied_at_start',
        ),
        migrations.AddField(
            model_name='round',
            name='shots',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]), default=list, size=5),
        ),
    ]
