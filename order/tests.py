from rest_framework import status
from rest_framework.test import APITestCase

from my_auth.models import CustomUser
from product.models import Product, ProductCategory


# Create your tests here.

class CreateOrderViewTest(APITestCase):
    def setUp(self):
        self.user1 = CustomUser.objects.create(
            username="TestUsername1",
            email="1@a.com",
            first_name="TestName",
            last_name="TestSurname",
            is_customer=True,
            is_seller=False
        )
        self.user1.set_password('Pas@w0rd')
        self.user1.save()

        self.user2 = CustomUser.objects.create(
            username="TestUsername2",
            email="2@a.com",
            first_name="TestName",
            last_name="TestSurname",
            is_customer=False,
            is_seller=False
        )
        self.user2.set_password('Pas@w0rd')
        self.user2.save()

        self.category = ProductCategory.objects.create(
            name="Test Category"
        )

        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=20.99,
            category=self.category,
            image=None
        )

        self.data = {
            'name': "TestName",
            "surname": "TestSurname",
            "products": {
                "1": 12
            },
            'address': "Test Address 1"
        }

    def test_create_order_not_logged_in(self):
        response = self.client.post('/orders/create/', self.data, format="json")
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_order_is_not_customer(self):
        self.client.login(username='TestUsername2', password='Pas@w0rd')
        response = self.client.post('/orders/create/', self.data, format="json")
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_order(self):
        test = self.client.login(username='TestUsername1', password='Pas@w0rd')
        response = self.client.post('/orders/create/', self.data, format="json")
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
