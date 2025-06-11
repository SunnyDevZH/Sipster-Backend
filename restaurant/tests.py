from django.test import TestCase
from .models import Restaurant
from categories.models import Category
from rest_framework.test import APIClient

class RestaurantModelTest(TestCase):
    """
    Unit Test (Modultest):
    Testet einzelne Model-Funktionalität isoliert.
    Hier: Erzeugung eines Restaurants mit Kategorie und deren String-Repräsentation.
    """
    def test_create_restaurant(self):
        cat = Category.objects.create(name="Bar")
        rest = Restaurant.objects.create(
            name="TestBar",
            description="Testdesc",
            price="$$",
        )
        rest.categories.add(cat)
        self.assertEqual(rest.name, "TestBar")
        self.assertIn(cat, rest.categories.all())
        self.assertEqual(str(rest), "TestBar")

class RestaurantAPITest(TestCase):
    """
    Integration Test:
    Testet das Zusammenspiel mehrerer Komponenten.
    Hier: API-Endpunkt /api/restaurants/ liefert die korrekten Restaurants zurück.
    """
    def setUp(self):
        cat = Category.objects.create(name="Bar")
        rest = Restaurant.objects.create(
            name="TestBar",
            description="Testdesc",
            price="$$",
        )
        rest.categories.add(cat)

    def test_restaurant_list_api(self):
        client = APIClient()
        response = client.get('/api/restaurants/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "TestBar")
