from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from core.forms import JoinForm, LoginForm
from core.models import Group, PendingGroup
from . import models
from . import forms
from django.test import TestCase, Client
from user.models import UserProfile
from django.url import reverse
from unittest import mock
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
        self.username = 'testUser1'
        self.password = '12345'
        user1 = User.objects.create(username=self.username)
        user1.set_password(self.password)
        user1.save()
        self.username = 'testUser2'
        self.password = '12345'
        user2 = User.objects.create(username=self.username)
        user2.set_password(self.password)
        user2.save()
        self.username = 'testUser3'
        self.password = '12345'
        user3 = User.objects.create(username=self.username)
        user3.set_password(self.password)
        user3.save()
        self.username = 'testUser4'
        self.password = '12345'
        user4 = User.objects.create(username=self.username)
        user4.set_password(self.password)
        user4.save()
        group1 = Group.objects.create(
                group_number=1,
                game_master= 'Reed',
                group_name='Looking-For-Game',
                campaign='Avernus',
                group_size='5',
                age_minimum="18+",
                experience_level="Intermediate",
                meeting_frequencies="Weekly",
                group_description="This is a test group for tests.",
                schedule="Friday at noon"
                )
        pgroup2 = PendingGroup.objects.create(
                pending_group_id='Test_Pending_Group',
                group_leader = user1,
                users=( user1, user2, user3, user4 )
                group = group1
                )
        url = reverse('profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/profile.html')
        self.assertContains(response, 'TestUser2')
    def Test_Profile_GroupView(self):
        group1 = Group.objects.create(
                group_number=1,
                game_master= 'Reed',
                group_name='Looking-For-Game',
                campaign='Avernus',
                group_size='5',
                age_minimum="18+",
                experience_level="Intermediate",
                meeting_frequencies="Weekly",
                group_description="This is a test group for tests.",
                schedule="Friday at noon"
                )
        url = reverse('groupview')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'component/groupview.html')
        self.assertContains(response, 1)
    def TestProfile_del(self):
        group1 = Group.objects.create(
                group_number=1,
                game_master= 'Reed',
                group_name='Looking-For-Game',
                campaign='Avernus',
                group_size='5',
                age_minimum="18+",
                experience_level="Intermediate",
                meeting_frequencies="Weekly",
                group_description="This is a test group for tests.",
                schedule="Friday at noon"
                )
        response = self.client.delete(self.group1, json.dumps({
            'id': 1
            }))
        url = reverse('profile')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/profile.html')
        self.assertEquals(response.Group.objects.count(), 0)
    def Test_about_Us(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/about.html')
    def Test_lfg(self):
        group1 = Group.objects.create(
                group_number=1,
                game_master= 'Reed',
                group_name='Looking-For-Game',
                campaign='Avernus',
                group_size='5',
                age_minimum="18+",
                experience_level="Intermediate",
                meeting_frequencies="Weekly",
                group_description="This is a test group for tests.",
                schedule="Friday at noon"
                )
        url = reverse('lfg')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/lfg.html')
        self.assertContains(response, 'Looking-For-Game')
    def Test_lfg_group(self):
        self.username = 'testUser1'
        self.password = '12345'
        user1 = User.objects.create(username=self.username)
        user1.set_password(self.password)
        user1.save()
        self.username = 'testUser2'
        self.password = '12345'
        user2 = User.objects.create(username=self.username)
        user2.set_password(self.password)
        user2.save()
        self.username = 'testUser3'
        self.password = '12345'
        user3 = User.objects.create(username=self.username)
        user3.set_password(self.password)
        user3.save()
        self.username = 'testUser4'
        self.password = '12345'
        user4 = User.objects.create(username=self.username)
        user4.set_password(self.password)
        user4.save()
        group1 = Group.objects.create(
                group_number=1,
                game_master= 'Reed',
                group_name='Looking-For-Game',
                campaign='Avernus',
                group_size='5',
                age_minimum="18+",
                experience_level="Intermediate",
                meeting_frequencies="Weekly",
                group_description="This is a test group for tests.",
                schedule="Friday at noon"
                )
        pgroup2 = PendingGroup.objects.create(
                pending_group_id='Test_Pending_Group',
                group_leader = user1,
                users=( user1, user2, user3, user4 )
                group = group1
                )
        url = reverse('request_group')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'component/request_group.html')
        self.assertContains(response, 'Looking-For-Game')
        url = reverse('lfg')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/lfg.html')
        self.assertContains(response, 'TestUser3')
    def Test_sort_age(self):
        group1 = Group.objects.create(
                group_number=1,
                game_master= 'Reed',
                group_name='Looking-For-Game',
                campaign='Avernus',
                group_size='5',
                age_minimum="18+",
                experience_level="Intermediate",
                meeting_frequencies="Weekly",
                group_description="This is a test group for tests.",
                schedule="Friday at noon"
                )
        url = reverse('lfg')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/lfg.html')
        self.assertContains(response, '18+')
    def Test_sort_exp(self):
        group1 = Group.objects.create(
                group_number=1,
                game_master= 'Reed',
                group_name='Looking-For-Game',
                campaign='Avernus',
                group_size='5',
                age_minimum="18+",
                experience_level="Intermediate",
                meeting_frequencies="Weekly",
                group_description="This is a test group for tests.",
                schedule="Friday at noon"
                )
        url = reverse('lfg')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/lfg.html')
        self.assertContains(response, 'Intermediate')
    def Test_sort_players(self):
        group1 = Group.objects.create(
                group_number=1,
                game_master= 'Reed',
                group_name='Looking-For-Game',
                campaign='Avernus',
                group_size='5',
                age_minimum="18+",
                experience_level="Intermediate",
                meeting_frequencies="Weekly",
                group_description="This is a test group for tests.",
                schedule="Friday at noon"
                )
        url = reverse('lfg')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/lfg.html')
        self.assertContains(response, '4-6')
    def TestLogin_No_Data(self):
        login = LoginFrom(data={})
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'component/login.html')
        self.assertFalse(login.is_valid())
    def TestLogin_With_Data(self):
        login = LoginForm(data={
            'username' : 'Bobukus'
            'password' : '246810'
            })
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'component/login.html')
        self.assertTrue(login.is_valid())
    def TestJoin_No_Data(self):
        join = JoinForm(data={})
        url = reverse('join')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'component/join.html')
        self.assertFalse(join.is_valid())
    def TestJoin_With_Data(self):
        join = JoinForm(data={
            'password' : '246810',
            'email' : 'Bobukus@gmail.com',
            })
        url = reverse('join')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'component/join.html')
        self.assertTrue(join.is_valid())
    def Test_logout(self):
        self.username = 'testUser1'
        self.password = '12345'
        user1 = User.objects.create(username=self.username)
        user1.set_password(self.password)
        user1.save()
        user1.logout()
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/lfg.html')
    def Test_Create_Group(self):
        group1 = Group.objects.create(
                group_number=1,
                game_master= 'Reed',
                group_name='Looking-For-Game',
                campaign='Avernus',
                group_size='5',
                age_minimum="18+",
                experience_level="Intermediate",
                meeting_frequencies="Weekly",
                group_description="This is a test group for tests.",
                schedule="Friday at noon"
                )
        createGroup = CreateGroupForm(data= {
            'model' : group1
            })
        url = reverse('create_group')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'component/create_group.html')
        self.assertTrue(createGroup.is_valid())
    def Test_Group_Page(self):
        gPage = data{
                'username': 'Bobulius',
                'groupname': 'TestCaseQuest',
                'room_name': 6
                }
        url = reverse('group_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/group_page.html')
        self.assertContains(response, 'Bobulius')
