from django.core.management.base import BaseCommand
from telegram_bot.bot import run_bot
from django.conf import settings

class Command(BaseCommand):
    help = 'Runs the Telegram bot'

    def handle(self, *args, **options):
        bot_token = settings.TELEGRAM_BOT_TOKEN
        self.stdout.write(self.style.SUCCESS('Starting Telegram bot...'))
        run_bot(bot_token)