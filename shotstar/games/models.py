from django.db import models
from django.contrib.postgres.fields import ArrayField, IntegerRangeField

# from accounts.models import User


class Game(models.Model):
    # creator_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_played = models.DateField(null=True)
    number_of_players = IntegerRangeField()
    creator_station_start = IntegerRangeField()
    video = models.FileField(upload_to='videos/%Y/%m/%d/', blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Game ID: {self.id}-Creator ID: {self.creator_id} \
        -Date Played: {self.date_played}'


class Round(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    # player_ids = models.ManyToManyField(User, on_delete=models.SET_NULL)
    round_number = IntegerRangeField()

    def __str__(self):
        return f'Round ID: {self.id}-Game ID: {self.game_id}'


class Shot(models.Model):
    round_id = models.ForeignKey(Round, on_delete=models.CASCADE)
    shot_number = IntegerRangeField()
    station_number = IntegerRangeField()
    hit_or_miss = IntegerRangeField()

    def __str__(self):
        return f'Shot ID: {self.id}-Hit or Miss: {self.hit_or_miss}'
