from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from user.models import UserProfile

#CHOICES
SIZE_CHOICES = (
    ("2-3", "2-3"),
    ("4-6", "4-6"),
    ("7+", "7+"),
)

AGE_CHOICES = (
    ("any", "Any age"),
    ("13+", "13+"),
    ("18+", "18+"),
)

EXP_CHOICES = (
    ("beginner", "Beginner"),
    ("intermediate", "Intermediate"),
    ("advanced", "Advanced"),
)

FREQ_CHOICES = (
    ("twice weekly", "Twice Weekly"),
    ("weekly", "Weekly"),
    ("twice monthly", "Twice Monthly"),
    ("montly", "Monthly"),
    ("other", "Other"),
)

class Group(models.Model):
        #group_number = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE)
        group_number = models.IntegerField(null=True);
        game_master = models.CharField(max_length = 240, default="Game Master")
        group_name = models.CharField(max_length = 240)
        campaign = models.CharField(max_length = 240)
        group_size = models.CharField(max_length = 20, choices= SIZE_CHOICES, default = "5")
        age_minimum = models.CharField(max_length = 20, choices = AGE_CHOICES, default = "18+")
        experience_level = models.CharField(max_length = 20, choices = EXP_CHOICES, default = "Intermediate")
        meeting_frequencies = models.CharField(max_length = 20, choices = FREQ_CHOICES, default = "Weekly")
        group_description = models.CharField(max_length = 240)
        schedule = models.CharField(max_length = 240)
        #members = models.ManyToManyField(UserProfile, through='PendingGroup',related_name='%(class)s_requests_created')


class PendingGroup(models.Model):
    pending_group_id = models.CharField(max_length=30)
    group_leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name="leader")
    users = models.ManyToManyField(User)
    #group = models.CharField(max_length=10)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="orig_group_number")
    #person = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    #group = models.ForeignKey(Group, on_delete=models.CASCADE)

class MessageModel(models.Model):
    sender = models.TextField()
    message_text = models.TextField()
    time = models.TextField(null=True)
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.sender

    def recent_messages(self):
        return MessageModel.objects.order_by('time').all()[:50]
