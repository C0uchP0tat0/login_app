from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .serializers import UserSerializer

client = APIClient()


class UserProfileTestCase(APITestCase):
    def setUp(self):
        # создайте нового пользователя, отправив запрос к конечной точке djoser
        self.user1 = User.objects.create_user(username='test1', password='test1')
        self.user2 = User.objects.create_user(username='test2', password='test2')

    def test_get_all_accounts(self):
        # получаем список всех созданых пользователей
        response = client.get(reverse('accounts'))
        accounts = User.objects.all()
        serializer = UserSerializer(accounts, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_account(self):
        # проверяем существование пользователя
        response = client.get(reverse('my', kwargs={'pk': self.user1.pk}))
        account = User.objects.get(pk=self.user1.pk)
        serializer = UserSerializer(account)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_account(self):
        # проверяем отсутвие пользователя
        response = client.get(reverse('my', kwargs={'pk': 10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_register(self):
        data = {
            'username': 'test_user',
            'password': 'qwerty123',
            'password2': 'qwerty123',
        }
        response = client.post(reverse('signup'), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# TODO написать или актуализировать тесты для списка пользователей и одного пользователя
