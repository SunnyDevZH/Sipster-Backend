from django.test import TestCase
from .models import Category
from rest_framework.test import APIClient

class CategoryModelTest(TestCase):
    """
    Unit Test (Modultest):
    Testet einzelne Model-Funktionalität isoliert.
    Hier: Erzeugung einer Kategorie und deren String-Repräsentation.
    """
    def test_create_category(self):
        cat = Category.objects.create(name="Bar", image="test.jpg")
        self.assertEqual(cat.name, "Bar")
        self.assertEqual(str(cat), "Bar")


class CategoryAPITest(TestCase):
    """
    Integration Test:
    Testet das Zusammenspiel mehrerer Komponenten.
    Hier: API-Endpunkt /api/categories/ liefert die korrekten Kategorien zurück.
    """
    def setUp(self):
        Category.objects.create(name="Bar")
        Category.objects.create(name="Club")

    def test_category_list_api(self):
        client = APIClient()
        response = client.get('/api/categories/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

        names = [category['name'] for category in response.data]
        self.assertIn("Bar", names)
        self.assertIn("Club", names)
