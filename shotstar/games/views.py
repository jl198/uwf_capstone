from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Game


def index(request):
    games = Game.objects.all().filter(creator_id=request.user)
    rounds = []
    for round in Game.objects.all().values_list(
            'id',
            'rounds__round_number',
            'rounds__station_number',
            'rounds__shots_taken'
    ).order_by(
        'id',
        'rounds__round_number'
    ):
        game_id, round_num, station_num, shots_taken = round
        shots_taken = {int(key): int(value) for key, value in
                       shots_taken.items()}
        new_round = [game_id, round_num, station_num, shots_taken]
        rounds.append(new_round)

    paginator = Paginator(games, 6)
    page = request.GET.get('page')
    paged_games = paginator.get_page(page)
    context = {
        'games': paged_games,
        'rounds': rounds
    }

    return render(request, 'games/games.html', context)


def game(request, game_id):
    return render(request, 'games/game.html')


def create_game(request):
    return render(request, 'games/create_game.html')
