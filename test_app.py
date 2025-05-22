import unittest
from app import app
import werkzeug

# Patch temporário para adicionar o atributo '__version__' em werkzeug
if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Criação do cliente de teste
        cls.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "API is running"})

    def test_login(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json)

    def test_protected_no_token(self):
        response = self.client.get('/protected')
        self.assertEqual(response.status_code, 401)



##########################################################################################################

    def test_login_access_token_is_string(self):
        response = self.client.post('/login')
        token = response.json.get("access_token")
        self.assertIsInstance(token, str)


    def test_route_not_found(self):
        response = self.client.get('/rota-invalida')
        self.assertEqual(response.status_code, 404)

    def test_items_route(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)

        # Verifica se é JSON
        self.assertTrue(response.is_json)

        data = response.get_json()

        # Verifica se contém a chave "items"
        self.assertIn("items", data)

        # Verifica se é uma lista com os itens esperados
        self.assertIsInstance(data["items"], list)
        self.assertListEqual(data["items"], ["item1", "item2", "item3"])

if __name__ == '__main__':
    unittest.main()
