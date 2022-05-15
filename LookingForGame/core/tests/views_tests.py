from django.contrib.auth.models import User
from django.test import TestCase, Client
import json


class TestViews(TestCase):
    def Testlogin(self, data):
        self.username = 'testUser'
        self.password = '12345'
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()

        c = Clients()
        UserLogIn = c.login(username=self.username, password=self.password)
        self.assertTrue(UserLogIn)
    def TestProfile():
        force_login(user, backend=None)
