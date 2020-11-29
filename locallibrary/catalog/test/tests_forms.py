from django.test import SimpleTestCase
from catalog.forms import GameForm

class TestForms(SimpleTestCase):
    
    def test_game_form_valid_data(self):
        form = GameForm(data={
            'title': 'Dark Souls 3',
            'developer': 'Software',
            'description': 'A very hard game',
            'genre': 'soul',
            'plataform': 'Playstation',
            'players': '1',
            'price': '$20.000',
            'img': 'asd'
        })

        self.assertTrue(form.is_valid())
