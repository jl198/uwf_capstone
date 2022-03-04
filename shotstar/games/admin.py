from django.contrib import admin

from .models import *


class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'creator_id', 'date_played', 'number_of_players',)
    list_display_links = ('id',)
    list_filter = ('creator_id', 'date_played', 'number_of_players',)


class RoundAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'player_id',
        'round_number',
        'station_number',
        'shots',
    )
    list_display_links = ('id', 'player_id')
    list_filter = ('id', 'player_id', 'round_number', 'station_number',)


admin.site.register(Game, GameAdmin)
admin.site.register(Round, RoundAdmin)
