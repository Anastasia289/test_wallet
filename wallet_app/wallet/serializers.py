from django.db.models import F
from rest_framework import serializers

from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ["uuid", "balance"]

    def validate(self, data):
        operation_type = self.initial_data.get("operation_type")
        amount = self.initial_data.get("amount")
        balance = self.initial_data.get("balance")

        if operation_type != "DEPOSIT" and operation_type != "WITHDRAW":
            raise serializers.ValidationError(
                "Неверная операция, может быть только DEPOSIT или WITHDRAW"
            )

        if operation_type == "WITHDRAW" and balance < amount:
            raise serializers.ValidationError("Недостаточно средств")

        return data

    def make_transaction(
        self,
    ):
        wallet = self.context["wallet"]
        operation_type = self.initial_data["operation_type"]
        amount = self.initial_data["amount"]
        if operation_type == "WITHDRAW":
            wallet.balance = F("balance") - amount
        else:
            wallet.balance = F("balance") + amount

        wallet.save(update_fields=["balance"])
        wallet.refresh_from_db()
        return wallet
