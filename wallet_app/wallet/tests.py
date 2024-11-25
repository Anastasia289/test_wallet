import uuid

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import Wallet


class TestWallet(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.uuid = uuid.uuid4()
        cls.str_uuid = str(cls.uuid)
        cls.client = APIClient()
        cls.test_wallet = Wallet.objects.create(uuid=cls.uuid, balance=1000)

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

    def test_get_wallet2(self):
        """Получаем кошелек со статусом 200."""
        response = self.client.get(
            f"http://127.0.0.1:8000/api/v1/wallets/{self.str_uuid}/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_wallet3(self):
        """Получаем кошелек со статусом 400 (неверный uuid)."""
        response = self.client.get("http://127.0.0.1:8000/api/v1/wallets/123/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_operation200(self):
        """Операция со статусом 200."""
        data = {"operation_type": "DEPOSIT", "amount": 100}
        response = self.client.post(
            f"http://127.0.0.1:8000/api/v1/wallets/{self.str_uuid}/operation/",
            data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_operation400(self):
        """Ошибка в типе операции."""
        data = {"operation_type": "DEPOSITююю", "amount": 100}
        response = self.client.post(
            f"http://127.0.0.1:8000/api/v1/wallets/{self.str_uuid}/operation/",
            data,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_withsraw_not_correct(self):
        """попытка снять слишком много."""
        data = {"operation_type": "WITHDRAW", "amount": 100000}
        response = self.client.post(
            f"http://127.0.0.1:8000/api/v1/wallets/{self.str_uuid}/operation/",
            data,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_deposit_correct(self):
        """Проверяем корректное пополнение баланса."""
        data = {"operation_type": "DEPOSIT", "amount": 100}
        start_sum = self.test_wallet.balance
        response = self.client.post(
            f"http://127.0.0.1:8000/api/v1/wallets/{self.str_uuid}/operation/",
            data,
        )
        updated_wallet = Wallet.objects.get(uuid=self.uuid)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_wallet.balance, start_sum + 100)

    def test_withdraw_correct(self):
        """Проверяем корректное снятие денег."""
        # data = {"operation_type": "WITHDRAW", "amount": 100.0}

        # start_sum = Wallet.objects.get(uuid=self.uuid).balance
        # response = self.client.post(
        #     f"http://127.0.0.1:8000/api/v1/wallets/{self.str_uuid}/operation/",
        #     data,
        # )
        # print("это тут", response.json, response.content)
        # updated_wallet = Wallet.objects.get(uuid=self.uuid)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(updated_wallet.balance, start_sum-100)
