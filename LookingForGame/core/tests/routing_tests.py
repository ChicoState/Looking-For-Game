from django.test import SimpleTestCase
from django.url import resolve, reverse
from . import Consumer


class TestRouting(SimpleTestCase):
    def test_chat_is_resolved(self):
        url = reverse('chat', args=['group1'])
        self.assertEqual(url, '/chat/group1/')
        resolver = resolve('/chat/')
        self.assertEqual(resolver.view_name, 'chat')
