
from django.contrib import admin
from .models import Player, Sport


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport', 'is_featured', 'is_top_player', 'verified')
    list_filter = ('is_featured', 'is_top_player', 'verified')


admin.site.register(Sport)