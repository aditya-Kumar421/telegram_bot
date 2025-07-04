# Generated by Django 5.2.3 on 2025-06-13 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramuser',
            name='telegram_id',
            field=models.BigIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
