
from flask_testing import TestCase
from server import get_app
import timeout_decorator

import json

class TestServer(TestCase):

    def create_app(self):
        app = get_app()
        app.config['TESTING'] = True
        return app

    @timeout_decorator.timeout(2)
    def test_hello_is_returned(self):
        response = self.client.get("/hello")

        json_response = json.loads(response.data.decode('utf8'))

        self.assertTrue('hello' in json_response)
        self.assertTrue(json_response['hello'] == "world")

    def test_products_are_returned(self):
        response = self.client.get("/api/products")

        json_response = json.loads(response.data.decode('utf8'))

        self.assertTrue('ids' in json_response)
        self.assertTrue('names' in json_response)
        self.assertEqual(len(json_response['ids']), 3)
        self.assertEqual(len(json_response['names']), 3)

    def test_products_are_filtered(self):
        response = self.client.get("/api/products/0")
        json_response = json.loads(response.data.decode('utf8'))
        self.assertTrue('rows' in json_response)
        self.assertEqual(len(json_response['rows']), 10)

        response = self.client.get("/api/products/1")
        json_response = json.loads(response.data.decode('utf8'))
        self.assertTrue('rows' in json_response)
        self.assertEqual(len(json_response['rows']), 10)
