from django.test import TestCase
from user.models import UserProfile
from django.contrib.auth.models import User
from core.models import Group

class TestModels(TestCase):
    def setUp(self):
        self.username = 'testUser'
        self.password = '12345'
        user1 = User.objects.create(username=self.username)
        user1.set_password(self.password)
        user1.save()
        self.username = 'testUser2'
        self.password = '54321'
        user2 = User.objects.create(username=self.username)
        user2.set_password(self.password)
        user2.save()
        self.group1 = Group.objects.create(
                group_number = 1,
                game_master = "Reed",
                group_name = "Test_Group_Name",
                campaign = "TestQuest",
                group_size = "6",
                age_minimum = "18+",
                experience_level = "beginner",
                meeting_frequencies = "Weekly",
                group_description = "This is a test group",
                schedule = "Meet on Fridays!"
                )
        self.pgroup2 = PendingGroup.objects.create(
                pending_group_id ="2",
                group_leader = user1,
                users = user2,
                group = self.group1
                )
        self.message = MessageModel.objects.create(
                sender = "Bob",
                message_text = "this is a test message",
                time = "12:35",
                group = self.group1
                )
        def test_group_built_correctly(self):
            self.assertEquals(self.group1.group_name, 'Test_Group_name')

        def test_pending_group_built_correctly(self):
            self.assertEquals(self.pgroup2.group_leader, 'TestUser')

        def test_message_built_correctly(self):
            self.assertEquals(self.message.message_text, 'this is a test message')
