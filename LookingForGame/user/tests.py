from django.test import TestCase
from django.apps import UserConfig

# Create your tests here.
# Test if URL is working.
class URLTests(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

#Tests apps
class AppsTest(UserConfig):
    def name_equals_user(self):
        self.assertEqual(name, 'user')
