# Generated by Django 4.2.7 on 2024-11-23 16:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Wallet UUID')),
                ('balance', models.FloatField()),
            ],
            options={
                'verbose_name': 'Wallet',
                'verbose_name_plural': 'Wallets',
            },
        ),
    ]
