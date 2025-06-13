from django.contrib import admin
from .models import TelegramUser
@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['telegram_id', 'username', 'created_at']
    search_fields = ['telegram_id', 'username']