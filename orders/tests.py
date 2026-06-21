from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class MyOrderViewTest(TestCase):

    def test_no_logged_user_should_redirect(self):
        url = reverse('my_order')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_logged_user_should_return_200(self):
        User = get_user_model()
        user = User.objects.create(username='testuser')
        self.client.force_login(user)
        url = reverse('my_order')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
