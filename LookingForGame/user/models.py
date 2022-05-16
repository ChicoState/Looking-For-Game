from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(primary_key=True, to=User, on_delete=models.CASCADE)
    #user = models.CharField(max_length=30)
    #username = models.CharField(max_length=16)
    email = models.CharField(max_length=30)

#    def __str__(self):
#        return str(user)+'s preferences'

class ThreadModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

class MessageModel(models.Model):
    thread = models.ForeignKey('ThreadModel', related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='', blank=True, null=True)
    #date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)