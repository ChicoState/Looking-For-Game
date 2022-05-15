from django.test import SimpleTestCase
from core.forms import JoinForm, LoginForm, CreateGroupForm
from core.models import Group
from user.models import UserProfile
from django.contrib.auth.models import User

class TestForms(SimpleTestCase):
    def Test_Forms_Valid_Data(self):
        self.username = 'testUserF'
        self.password = '246810'
        user1 = User.objects.create(username=self.username)
        user1.set_password(self.password)
        join = JoinForm(data= {
            'password': '12345',
            'email': 'mailAccount@gmail.com',
            'model': user1,
            'fields': ('Bob', 'Fake', 'FakusBobus', 'mailAccount@gmail.com', '12345')
            })
        self.assertTrue(join.is_valid())
        login = LoginForm(data= {
            'username' : 'Bobukus',
            'password' : '246810'
            })
        self.assertTrue(login.is_valid())
        self.group1 = Group.objects.create(
                group_number = 6,
                game_master = "Mega_DM",
                group_name = "Test_Form_Group",
                campaign = "TestQuest",
                group_size = "4",
                age_minimum = "18+",
                experience_level = "beginner",
                meeting_frequencies = "Weekly",
                schedule = "Meet every Saturday",
                group_description = "Test group for form testing"
                )
        gForm = CreateGroupForm(data= {
            'model': group1
            })
        self.assertTrue(gForm.is_valid())
    def Test_Forms_NO_Data(self):
        join = JoinForm(data={})
        self.assertFalse(join.is_valid())
        login = LoginForm(data={})
        self.assertFalse(login.is_valid())
        gForm = CreateGroupForm(data={})
        self.assertFalse(gForm.is_valid())
