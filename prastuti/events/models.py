from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import Profile


# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=20)
    team_size_mn = models.IntegerField(default=1)
    team_size_mx = models.IntegerField(default=4)
    # event_info = models.TextField()
    def __str__(self):
        return self.event_name

#need to create events here
