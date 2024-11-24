from django.contrib.auth.hashers import make_password
from django.db import migrations
import uuid
from wallet.models import Wallet
from django.contrib.auth import get_user_model


def add_wallets(apps, schema_editor):
   
    Wallet.objects.create(uuid=uuid.uuid4(), balance=1000)
    Wallet.objects.create(uuid=uuid.uuid4(), balance=2000)
    Wallet.objects.create(uuid=uuid.uuid4(), balance=5000)


class Migration(migrations.Migration):
    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_wallets),
    ]