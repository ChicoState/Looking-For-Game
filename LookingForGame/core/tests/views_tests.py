from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from core.forms import JoinForm, LoginForm
from core.models import Group, PendingGroup
from . import models
from . import forms
from django.test import TestCase, Client
from user.models import UserProfile
from django.url import reverse
import json


class TestViews(TestCase):
    def SetUp(self):
        force_login(user, backend=None)
        self.client = Client()
    def TestIndex(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')
    def Testlogin(self, data):
        self.username = 'testUser'
        self.password = '12345'
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()

        c = Client()
        UserLogIn = c.login(username=self.username, password=self.password)
        self.assertTrue(UserLogIn)
    def TestProfile(self):
        response = self.client.post(reverse('core/profile.html'), follow=True)
        assertRedirects(response, reverse('core/tests/views_tests.py'), target_status_code=200)
    def TestProfile_GroupView(self):
        response = self.client.get(group.objects)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'component/groupview.html')
    def TestProfile_del(self):
        group1 = Group.objects.create(
                group_number=1,
                game_master= 'Reed',
                group_name='Looking-For-Game',
                campaign='Avernus',
                group_size=5
                age_minimum="18+",
                experience_level="Intermediate",
                meeting_frequencies="Weekly",
                group_description="This is a test group for tests.",
                schedule="Friday at noon"
                )
        response = self.client.delete(self.group1,json.dumps({
            'id': 1
            }))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.Group.objects.count(), 0)



