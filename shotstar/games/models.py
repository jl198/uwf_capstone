from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import HStoreField
from django.core.validators import MaxValueValidator, MinValueValidator


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
    stations_occupied_at_start = HStoreField(null=True)

    creator_station_start = models.IntegerField(
        blank=True,
        null=True,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    video = models.FileField(upload_to='videos/%Y/%m/%d/', blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Game ID: {self.id}-Creator ID: {self.creator_id} \
        -Date Played: {self.date_played}'


class Round(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    player_ids = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        default=None
    )
    round_number = models.IntegerField(
        blank=True,
        null=True,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )

    def __str__(self):
        return f'Round ID: {self.id}-Game ID: {self.game_id}'


class Shot(models.Model):
    player_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        default=None
    )
    round_id = models.ForeignKey(Round, on_delete=models.CASCADE)
    shot_number = models.IntegerField(
        blank=False,
        null=False,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    station_number = models.IntegerField(
        blank=False,
        null=False,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    hit_or_miss = models.IntegerField(
        blank=False,
        null=False,
        validators=[MaxValueValidator(1), MinValueValidator(0)]
    )

    def __str__(self):
        return f'Shot ID: {self.id}-Hit or Miss: {self.hit_or_miss}'
