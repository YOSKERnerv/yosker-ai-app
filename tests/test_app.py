import unittest
from app import app  # Make sure `app` is defined in app/__init__.py or app.py

class BasicTests(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        # Assumes your app has a route at '/'
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        # Assumes your home route has a welcome message
        response = self.app.get('/')
        self.assertIn(b'Welcome', response.data)

if __name__ == "__main__":
    unittest.main()
