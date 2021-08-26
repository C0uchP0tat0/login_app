from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .views import accounts

class SigninTest(TestCase):
    def setUp(self):
        #Создание пользователя
        self.user = User.objects.create_user(username='test', password='12345')
        self.user.save()
    def tearDown(self):
        #Очистка тестовой базы
        self.user.delete()
    def test_correct(self):
        user = authenticate(username='test', password='12345')
        self.assertTrue(user is not None and user.is_authenticated)
    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12345')
        self.assertFalse(user is not None and user.is_authenticated)
    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

class ViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='12345')
        self.user.save()
        self.client.login(username='test', password='12345')
    def tearDown(self):
        self.user.delete()
    def test_no_tasks(self):
        response = self.client.get('')
        self.assertEqual(response.status_code,200)


