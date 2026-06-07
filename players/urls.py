from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from players.views import edit_player, player_profile, create_player, player_list

urlpatterns = [
    path('', player_list, name='player_list'),
    path('profile/<int:pk>/', player_profile, name='player_profile'),
    path('create/', create_player, name='create_player'),
    path('edit/<int:pk>/', edit_player, name='edit_player'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )