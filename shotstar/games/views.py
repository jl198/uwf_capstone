from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
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
    current_game = get_object_or_404(Game, pk=game_id)
    print(f'{current_game.video}')
    context = {
        'game': current_game
    }
    return render(request, 'games/game.html', context)


def new_game(request):
    # user = request.user.username
    # print(f'{user=}')
    # if user is not None and request.method == 'POST':
    #     # Get form values
    #     creator_id = request.user
    #     date_played = request.POST['date_played']
    #     number_of_players = request.POST['number_of_players']
    #     creator_station_start = request.POST['creator_station_start']
    #     video = request.POST['video']
    #
    #     new_game = Game.objects.create(
    #         creator_id=creator_id,
    #         date_played=date_played,
    #         number_of_players=number_of_players,
    #         creator_station_start=creator_station_start,
    #         video=video
    #     )
    #     new_game.save()
    #     messages.success(request, "Game successfully created!")
    #     return redirect('games')
    # else:
        return render(request, 'games/new_game.html')
