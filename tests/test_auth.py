import unittest
from app import app

class AuthTestCase(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()

	def test_login_page(self):
		response = self.app.get('/login')
		self.assersEqual(response.status_code, 200)
		self.assertIn(b'Login', response.data)

	def test_tegister_page(self):
		response = self.app.get('/register')
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Register', response.data)


