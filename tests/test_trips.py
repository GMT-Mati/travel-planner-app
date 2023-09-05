import unittest
from app import app

class TripTestCase(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()

	def test_trips_page(self):
		response = self.app.get('/trips')
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Trips', response.data)

	def test_create_trip_page(self):
		response = self.app.get('/create_trip')
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Create Trip', response.data)


