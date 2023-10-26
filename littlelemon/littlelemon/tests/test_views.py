from django.tests import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Menu

class MenuViewTest(TestCase):
    def setup(self):
        # Create test instances of the Menu model
        self.menu1 = Menu.objects.create(name="Item 1", price=10.99)
        self.menu2 = Menu.objects.create(name="Item 2", price=15.99)
        self.menu3 = Menu.objects.create(name="Item 3", price=8.99)

    def test_getall(self):
        # Initialize the client for making API requests
        client = APIClient()

        url = reverse('restaurant/booking') 

        # Make a GET request to the MenuView
        response = client.get(url)

        # Check if the response status code is HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the test data (in this example, we use a simple representation)
        expected_data = [
            {'name': 'Item 1', 'price': '10.99'},
            {'name': 'Item 2', 'price': '15.99'},
            {'name': 'Item 3', 'price': '8.99'},
        ]

        # Check if the response data matches the expected serialized data
        self.assertEqual(response.data, expected_data)
