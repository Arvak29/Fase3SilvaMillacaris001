from django.test import TestCase, Client
from django.urls import reverse
from catalog.models import Game, Plataform

class TestView(TestCase):

    def test_project_list_GET(self):
        client = Client()

        response = client.get(reverse('add_game'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_game.html')