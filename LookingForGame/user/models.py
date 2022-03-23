from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    id = models.OneToOneField(primary_key=True, to=User, on_delete=models.CASCADE)
    user = models.CharField(max_length=30)
    username = models.CharField(max_length=16)
    email = models.CharField(max_length=30)

#    def __str__(self):
#        return str(user)+'s preferences'
