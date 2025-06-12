import os
from celery import Celery
from decouple import config
# from dotenv import load_dotenv

# Load environment variables from .env file

# Set the default Django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tele_bot.settings')

# Configure Celery with Upstash Redis
# UPSTASH_REDIS_HOST = os.getenv('UPSTASH_REDIS_HOST')
# UPSTASH_REDIS_PORT = os.getenv('UPSTASH_REDIS_PORT')
# UPSTASH_REDIS_PASSWORD = os.getenv('UPSTASH_REDIS_PASSWORD')
UPSTASH_REDIS_HOST = config('UPSTASH_REDIS_HOST')
UPSTASH_REDIS_PORT = config('UPSTASH_REDIS_PORT')
UPSTASH_REDIS_PASSWORD = config('UPSTASH_REDIS_PASSWORD')

connection_link = f"rediss://{UPSTASH_REDIS_PASSWORD}@{UPSTASH_REDIS_HOST}:{UPSTASH_REDIS_PORT}?ssl_cert_reqs=required"



app = Celery('tele_bot', broker=connection_link, backend=connection_link)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()