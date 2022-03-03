from django.shortcuts import render


def index(request):
    return render(request, 'games/games.html')


def game(request):
    return render(request, 'games/game.html')


def create_game(request):
    return render(request, 'games/create_game.html')
