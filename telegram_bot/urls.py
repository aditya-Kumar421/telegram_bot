from django.urls import path
from .views import TelegramWebhookView, TelegramUserListAPIView

urlpatterns = [
    path('webhook/', TelegramWebhookView.as_view(), name='telegram-webhook'),
    path('users/', TelegramUserListAPIView.as_view(), name='telegram-users'),
]
