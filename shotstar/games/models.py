from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField


class Game(models.Model):
    creator_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=None,
        on_delete=models.CASCADE
    )
    date_played = models.DateField(blank=True, null=True)
    number_of_players = models.IntegerField(
        default=1,
        blank=False,
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    # stations_occupied_at_start = models.JSONField(default=dict)
    creator_station_start = models.IntegerField(
        blank=True,
        null=True,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    video = models.FileField(upload_to='videos/%Y/%m/%d/', blank=False,
                             null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return 'Game ID: ' + str(self.id) + \
    #            ' - Creator ID: ' + str(self.creator_id) + \
    #            ' - Date Played: ' + str(self.date_played)


class Round(models.Model):
    game_id = models.ForeignKey(
        Game,
        related_name='rounds',
        on_delete=models.CASCADE
    )
    player_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None
    )
    round_number = models.IntegerField(
        blank=True,
        null=True,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    station_number = models.IntegerField(
        blank=True,
        null=True,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    shots_taken = models.JSONField(default=dict)
    shots = ArrayField(
        models.IntegerField(
            default=0,
            blank=True,
            null=True,
            validators=[MaxValueValidator(1), MinValueValidator(0)]
        ),
        5,
        default=list
    )

    def __str__(self):
        return f'Round ID: {self.id}-Game ID: {self.game_id}'
