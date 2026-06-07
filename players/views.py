from django.shortcuts import render, redirect, get_object_or_404
from .models import Player
from .forms import PlayerForm
from django.contrib.auth.decorators import login_required





def player_list(request):
    players = Player.objects.select_related('sport', 'user').all()

    sport = request.GET.get('sport')
    location = request.GET.get('location')
    min_age = request.GET.get('min_age')
    max_age = request.GET.get('max_age')

    if sport:
        players = players.filter(sport__name__icontains=sport)

    if location:
        players = players.filter(location__icontains=location)

    if min_age:
        players = players.filter(age__gte=min_age)

    if max_age:
        players = players.filter(age__lte=max_age)

    players = players.order_by('-created_at')

    return render(request, 'players/list.html', {'players': players})



@login_required
def player_profile(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'players/player_profile.html', {'player': player})


@login_required
def create_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST  or None, request.FILES or None)


        if form.is_valid():
            player =form.save(commit=False)
            player.user = request.user
            player.save()
            return redirect('player_profile', pk=player.pk)
        else:
            return render(request, 'players/create_player.html', {'form': form})
    else:   
        form = PlayerForm()

@login_required
def edit_player(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_profile', pk=player.pk)
    else:
        form = PlayerForm(instance=player)
    return render(request, 'players/edit_player.html', {'form': form})