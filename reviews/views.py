from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewForm
from players.models import Player


def add_review(request, player_id):
    player = get_object_or_404(Player, id=player_id)

    form = ReviewForm(request.POST or None)

    if form.is_valid():
        review = form.save(commit=False)
        review.player = player
        review.reviewer = request.user
        review.save()
        return redirect('player_profile', pk=player.id)

    return render(request, 'reviews/add_review.html', {'form': form, 'player': player})