from django.contrib import admin

from .models import Wallet


class WalletAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        "balance",
    )
    empty_value_display = "-пусто-"


admin.site.register(Wallet, WalletAdmin)
