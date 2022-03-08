from django.db import models

class Group(models.Model):
        group_name = models.CharField(max_length = 240)
        campaign = models.CharField(max_length = 240)
        group_size = models.CharField(max_length = 240)
        age_minimum = models.CharField(max_length = 240)
        experience_level = models.CharField(max_length = 240)
        meeting_frequencies = models.CharField(max_length = 240)
        group_description = models.CharField(max_length = 240)
