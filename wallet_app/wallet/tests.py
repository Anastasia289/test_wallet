import uuid

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

# from rest_framework.response import Response
from rest_framework.test import APIClient

from .models import Wallet
from .serializers import WalletSerializer

# from .views import WalletViewSet


class TestWallet(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.uuid = uuid.uuid4()
        cls.client = APIClient()
        cls.test_wallet = Wallet.objects.create(uuid=cls.uuid, balance=1000)
        cls.test_wallet_serializer = WalletSerializer(cls.test_wallet)

    def test_get_wallet(self):
        """Наличие в базе созданного кошелька."""
        try:
            retrieved_wallet = Wallet.objects.get(uuid=self.uuid)
            self.assertEqual(
                self.test_wallet.uuid,
                retrieved_wallet.uuid,
                "Ошибка при получении uuid",
            )
            self.assertEqual(
                self.test_wallet.balance,
                retrieved_wallet.balance,
                "Ошибка при получении balance",
            )
        except Wallet.DoesNotExist:
            self.fail("Ошибка при получении кошелька.")

    def test_get_wallet_200(self):
        """Доступность созданного кошелька."""
        # url = reverse('wallet:', args=[self.test_wallet.uuid])
        url = reverse("wallet")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data, self.wallet_serializer.data)


# class WalletTestCase(TestCase):
#     def setUp(self):
#         self.uuid = uuid.uuid4()
#         self.client = APIClient()

#         self.wallet = Wallet.objects.create(uuid=self.uuid, balance=1000)

#         self.get_wallet_url = reverse('wallet', args=[self.wallet.uuid])

#         # self.get_wallet_url = reverse('wallets', kwargs={'uuid_wallet': str(self.wallet.uuid)})
#         # self.operation_url = reverse('wallet_operation', kwargs={'uuid': str(self.wallet.uuid)})


#     def test_get_wallet_success(self):
#         """Проверка успешного получения кошелька."""

#         response = self.client.get(self.get_wallet_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # self.assertEqual(response.data['uuid'], str(self.wallet.uuid))
#         # self.assertEqual(float(response.data['balance']), float(self.wallet.balance))
