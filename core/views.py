from django.shortcuts import render
from django.shortcuts import render
from players.models import Player


def home(request):
    featured_players = Player.objects.filter(is_featured=True)
    top_players = Player.objects.filter(is_top_player=True)

    latest_players = Player.objects.all().order_by('-created_at')[:6]

    return render(request, 'home.html', {
        'featured_players': featured_players,
        'top_players': top_players,
        'latest_players': latest_players
    })