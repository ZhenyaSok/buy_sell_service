from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from skymarket.ads.models import Ad
from .serializers import AdSerializer
from ..users.models import User


class AdViewSetsTestCase(APITestCase):

    def setUp(self) -> None:

        # Создадим тестовый аккаунт пользователя
        self.user = User.objects.create(email='test@yah.ru', password='123456')
        # Создадим тестовое объявление
        self.ad = Ad.objects.create(title='first ad', author=self.user, price=100, description='test')
        self.client.force_authenticate(user=self.user)  # Аутентификация пользователя
        # self.serializer_ad = AdSerializer([self.ad], many=True).data

    def test_get_queryset_authenticated_user(self):

        self.client.logout()
        url = reverse('ads:ads-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = AdSerializer([self.ad], many=True).data
        self.assertEqual(response.data, serializer_data)

    def test_get_queryset_unauthenticated_user(self):
        self.client.logout()
        url = reverse('ads:ads-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_ad_list(self):
        """Тест на получение листа приятных привычек"""

        response = self.client.get(reverse('ads:ads-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    # def test_ads_create(self):
    #
    #     """ Тест создания объявления """
    #
    #
    #     data = {
    #         "title": "1",
    #         "price": 10,
    #         "author": self.user.id,
    #         "description": "rdgf"
    #     }
    #
    #     response = self.client.post(
    #         reverse('ads:ads-list'),
    #         data=data
    #     )
    #
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #
    #     self.assertTrue(
    #         Ad.objects.all().exists()
    #     )
    #
    #     self.assertEqual(
    #         response.json()['title'],
    #         data['title']
    #     )

        # self.assertEqual(
        #     response.json()['price'],
        #     data['price']
        # )
        #
        # self.assertEqual(
        #     response.json()['description'],
        #     data['description']
        # )


    # def test_ads_update(self):
    #     """ ad updating testing"""
    #
    #     self.client.force_authenticate(user=self.user)
    #
    #     self.ad = Ad.objects.create(
    #         title="test",
    #         price=10,
    #         description="this is a creation test",
    #         author=self.user
    #     )
    #
    #     updated_data = {
    #         'title': 'test updated',
    #         'price': 15,
    #         "description": "this is a updated test"
    #     }
    #


