from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Product

class ProductListTest(TestCase):
    
    def test_should_return_200(self):
        User = get_user_model()
        user = User.objects.create(username='testuser')
        self.client.force_login(user)
        url = reverse('list_products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_should_return_200_with_products(self):
        User = get_user_model()
        user = User.objects.create(username='testuser2')
        self.client.force_login(user)
        Product.objects.create(
            name='Cappuccino',
            description='Café con leche',
            price=3.50,
            available=True,
            stock=10
        )
        url = reverse('list_products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['products'].count(), 1)