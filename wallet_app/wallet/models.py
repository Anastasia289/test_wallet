import uuid

from django.db import models


class Wallet(models.Model):
    uuid = models.UUIDField(
        "Wallet UUID", primary_key=True, default=uuid.uuid4, editable=False
    )
    balance = models.FloatField()

    class Meta:
        verbose_name = "Wallet"
        verbose_name_plural = "Wallets"

    def __str__(self) -> str:
        return f"{self.uuid} - {self.balance}"
