from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from user.models import UserProfile

class Group(models.Model):
        group_number = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE)
        game_master = models.CharField(max_length = 240, default="Game Master")
        group_name = models.CharField(max_length = 240)
        campaign = models.CharField(max_length = 240)
        group_size = models.CharField(max_length = 240)
        age_minimum = models.CharField(max_length = 240)
        experience_level = models.CharField(max_length = 240)
        meeting_frequencies = models.CharField(max_length = 240)
        group_description = models.CharField(max_length = 240)
