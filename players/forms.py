from django import forms
from .models import Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'sport',
            'position',
            'age',
            'height',
            'weight',
            'location',
            'bio',
            'experience',
            'profile_image',
            'highlight_video'
        ]