from rest_framework import status
from rest_framework.test import APITestCase

from my_auth.models import CustomUser


# Create your tests here.

class RegisterUserViewTest(APITestCase):
    def setUp(self):
        self.data = {
            'username': 'bRcqdvy9FwjzK@qrK.2VwNo+ucK0uD.ZEcjVcZ._BEu.1999mLl3I4Fa5kn7TDGaYpyMTj.t0qUe+',
            'password': 'Pas@w0rd',
            'password2': 'Pas@w0rd',
            'email': 'user@example.com',
            'first_name': 'string',
            'last_name': 'string',
            'is_seller': True,
            'is_customer': False
        }

    def test_register(self):
        response = self.client.post('/auth/register/', self.data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)


class LoginUserViewTest(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username='username', password='Pas@w0rd')

    def test_login(self):
        data = {
            'username': 'username',
            'password': 'Pas@w0rd'
        }
        response = self.client.post('/auth/login/', data)
        self.assertEquals(response.status_code, status.HTTP_202_ACCEPTED)
