from django.test import Client, TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser
from plantsitting.models import Owner, Plant

class ViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        user = Owner.objects.create_user(email='testuser@testuser.fr', username='testuser', password='testpassword')
        Plant.objects.create(name='maplante', owner = user, ltn=10.0, lgt=11.0)

    def test_display_root_app(self):
        response = self.client.get('/')
        self.assertEquals(404, response.status_code)

    def test_display_plant(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse('plants tpl'))
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertEquals(200, response.status_code)


    def test_custom_login(self):
        # Use the custom login view to simulate a user login
        response = self.client.post(reverse('custom_login'), {'username': 'testuser', 'password': 'testpassword'}, follow=True)
        self.assertEquals(200, response.status_code)
        # Check if the user is authenticated after login
        self.assertTrue(response.context['user'].is_authenticated, "User should be authenticated")