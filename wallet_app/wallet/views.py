from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from wallet.models import Wallet

from .serializers import WalletSerializer


class WalletViewSet(viewsets.ModelViewSet):
    """Wallet."""

    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    http_method_names = [
        "get",
        "post",
    ]

    @action(
        detail=True,
        methods=["post"],
        url_path="operation",
    )
    @transaction.atomic
    def transactions(self, request, pk):
        """Рц."""
        try:
            wallet = get_object_or_404(
                Wallet.objects.select_for_update(), uuid=pk
            )
            serializer = WalletSerializer(
                data={
                    "uuid": wallet.uuid,
                    "balance": wallet.balance,
                    "operation_type": request.data.get("operation_type"),
                    "amount": request.data.get("amount"),
                },
                context={"request": request, "wallet": wallet},
            )
            serializer.is_valid(raise_exception=True)
            wallet = serializer.make_transaction()
            return Response(
                f"""Баланс обновлен,
                текущий баланс на кошельке {wallet.uuid}
                составляет {wallet.balance}""",
                status=status.HTTP_200_OK,
            )

        except Exception as error:
            return Response(
                f"Некорректный запрос, {error}",
                status=status.HTTP_400_BAD_REQUEST,
            )
