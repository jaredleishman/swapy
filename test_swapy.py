import unittest
import responses
from unittest.mock import patch
from io import StringIO
from swapy import get_starships_with_pilots

class TestSwapi(unittest.TestCase):

    @responses.activate
    def test_hello(self):
        responses.add(
            responses.GET, 
            'https://swapi.dev/api/starships',
            json={
                'results': [
                    {
                        "name": "Death Star",
                        "pilots": [
                            'https://swapi.dev/api/starships/1'
                        ]
                    }
                ]
            }, 
            status=200
        )

        responses.add(
            responses.GET,
            'https://swapi.dev/api/starships/1',
            json={
                "name": "Emporer Palpatine"
            },
            status=200
        )

        with patch('sys.stdout', new = StringIO()) as fake_out:
            get_starships_with_pilots()
            self.assertEqual(fake_out.getvalue(), 'Death Star\n\tPilots: Emporer Palpatine\n')

if __name__ == '__main__':
    unittest.main()