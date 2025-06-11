from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

class UserModelTest(TestCase):
    """
    Unit Test (Modultest):
    Testet einzelne Model-Funktionalität isoliert.
    Hier: Erzeugung eines Users und dessen String-Repräsentation.
    """
    def test_create_user(self):
        user = User.objects.create_user(username="testuser", password="testpass")
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.check_password("testpass"))

class UserAPITest(TestCase):
    """
    Integration Test:
    Testet das Zusammenspiel mehrerer Komponenten.
    Hier: Registrierung, Login und Abruf der User-Details via API.
    """
    def setUp(self):
        self.user = User.objects.create_user(username="apitest", password="apipass")
        self.client = APIClient()

    def test_login_and_get_user(self):
        # Login (Token holen)
        response = self.client.post('/api/user/login/', {'username': 'apitest', 'password': 'apipass'})
        self.assertEqual(response.status_code, 200)
        access = response.data['access']

        # User-Details abrufen
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access)
        response = self.client.get('/api/user/me/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'apitest')
