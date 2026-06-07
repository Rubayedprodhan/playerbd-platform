from django.db import models
from django.conf import settings


class Sport(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Player(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    sport = models.ForeignKey(Sport,on_delete=models.SET_NULL,null=True)

    position = models.CharField(max_length=100)

    age = models.PositiveIntegerField()

    height = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)

    weight = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    location = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    experience = models.PositiveIntegerField(help_text="Years of experience")
    profile_image = models.ImageField(upload_to="players/",blank=True,null=True)

    highlight_video = models.URLField(blank=True)

    verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    
    is_featured = models.BooleanField(default=False)
    is_top_player = models.BooleanField(default=False)
    total_rating = models.FloatField(default=0)

   

    def __str__(self):
        return self.user.username
    

@property
def avg_rating(self):
    reviews = self.reviews.all()
    if reviews:
        return round(sum(r.rating for r in reviews) / reviews.count(), 1)
    return 0