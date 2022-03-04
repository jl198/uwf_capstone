# Generated by Django 4.0.3 on 2022-03-04 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_remove_round_player_ids_round_player_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='game_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rounds', to='games.game'),
        ),
    ]