from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from user.models import UserProfile

class Group(models.Model):
        #group_number = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE)
        group_number = models.IntegerField(null=True);
        game_master = models.CharField(max_length = 240, default="Game Master")
        group_name = models.CharField(max_length = 240)
        campaign = models.CharField(max_length = 240)
        group_size = models.CharField(max_length = 240)
        age_minimum = models.CharField(max_length = 240)
        experience_level = models.CharField(max_length = 240)
        meeting_frequencies = models.CharField(max_length = 240)
        group_description = models.CharField(max_length = 240)
        #members = models.ManyToManyField(UserProfile, through='PendingGroup',related_name='%(class)s_requests_created')


class PendingGroup(models.Model):
    person = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class MessageModel(models.Model):
    sender = models.TextField()
    message_text = models.TextField()
    time = models.TextField(null=True)
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.sender

    def recent_messages(self):
        return MessageModel.objects.order_by('time').all()[:50]