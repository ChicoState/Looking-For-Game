from django.test import TestCase

class TestModels(TestCase):
    def setUp(self):
        self.group1 = Group.objects.create(
                )
