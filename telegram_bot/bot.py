from telegram.ext import Application, CommandHandler
from telegram_bot.models import TelegramUser
from asgiref.sync import sync_to_async
import pytz

async def start(update, context):
    user = update.effective_user
    telegram_id = str(user.id)
    username = user.username or ""

    # Wrap synchronous database operation in sync_to_async
    await sync_to_async(TelegramUser.objects.update_or_create)(
        telegram_id=telegram_id,
        defaults={'username': username}
    )

    await update.message.reply_text(f"Hello {username or 'User'}! Your details are saved.")

def run_bot(token):
    application = Application.builder().token(token).persistence(None).build()
    application.add_handler(CommandHandler("start", start))
    # Set timezone to avoid apscheduler issues
    application.job_queue.scheduler.configure(timezone=pytz.timezone('Asia/Kolkata'))
    application.run_polling(allowed_updates=["message"], drop_pending_updates=True)