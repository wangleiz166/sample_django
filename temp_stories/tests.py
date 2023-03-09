from django.test import TestCase
from django.urls import reverse
from . import views


class TestIndexView(TestCase):
    
    def test_index_view_get(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'temp_stories/index.html')
        self.assertContains(response, 'culminating in a struggle at')


    def test_index_view_post(self):
        url = reverse('index')
        response = self.client.post(url, {'temp': '80'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'temp_stories/index.html')
        self.assertContains(response, 'culminating in a struggle at')
        self.assertContains(response, 'Your converted temperature of 80 in F is 26.668799999999997 in C')
