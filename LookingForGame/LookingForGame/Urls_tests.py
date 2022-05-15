from django.test import SimpleTestCase
from django.urls import reverse, resolve

class TestUrls(SimpleTestCase):
    def test_url_pattern(self):
        resolver = resolve('')
        self.assertEqual(resolver.view_name, '')
        
        resolver = resolve('profile/')
        self.assertEqual(resolver.view_name, 'profile')

        url = reverse('profile/groupview/', args=[13])
        self.assertEqual(url, '/profile/groupview/13/')
        resolver = resolve('/groupview/')
        self.assertEqual(resolver.view_name, 'groupview')

        url = reverse('profile/delete/', args=[13])
        self.assertEqual(url, '/profile/delete/13/')
        resolver = resolve('/delete/')
        self.assertEqual(resolver.view_name, 'delete')

        resolver = resolve('about/')
        self.assertEqual(resolver.view_name, 'about')

        resolver = resolve('lfg/')
        self.assertEqual(resolver.view_name, 'lfg')

        url = reverse('lfg/', args=[13])
        self.assertEqual(url, '/lfg/13/')
        resolver = resolve('lfg_group')
        self.assertEqual(resolver.view_name, 'lfg_group')

        url = reverse('lfg/sort_a/', 18+)
        self.assertEqual(url, '/lfg/sort_a/18+/')
        resolver = resolve('sort_a')
        self.assertEqual(resolver.view_name, 'sort_a')

        url = reverse('lfg/sort_p/', Bob)
        self.assertEqual(url, '/lfg/player/Bob/')
        resolver = resolve('sort_p')
        self.assertEqual(resolver.view_name, 'sort_p')

        url = reverse('lfg/sort_e/', beginner)
        self.assertEqual(url, '/lfg/sort_e/beginner/')
        resolver = resolve('sort_e')
        self.assertEqual(resolver.view_name, 'sort_e')

        resolver = resolve('admin/')
        self.assertEqual(resolver.view_name, 'admin')

        resolver = resolve('join/')
        self.assertEqual(resolver.view_name, 'join')

        resolver = resolve('login/')
        self.assertEqual(resolver.view_name, 'login')

        resolver = resolve('logout/')
        self.assertEqual(resolver.view_name, 'logout')

        resolver = resolve('create_group/')
        self.assertEqual(resolver.view_name, 'create_group')

        resolver = resolve('user/')
        self.assertEqual(resolver.view_name, 'user')

        resolver = resolve('preferences/')
        self.assertEqual(resolver.view_name, 'proferences')

        url = reverse('room', Avernus)
        self.assertEqual(url, '/profile/groupview/Group/Avernus/')
        resolver = resolve('Group')
        self.assertEqual(resolver.view_name, 'Group')
