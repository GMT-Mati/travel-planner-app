import unittest
from app import app

class DestinationsTestCase(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()

	def test_destinations_page(self):
		response = self.app.get('/destinations')
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Destinations', response.data)

	def test_add_destination_page(self):
		response = self.app.get('/add_destination')
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Add Destination', response.data)


