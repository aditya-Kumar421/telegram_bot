from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import TelegramUser
from .serializers import TelegramUserSerializer
from rest_framework.permissions import IsAuthenticated
class TelegramWebhookView(APIView):
    def post(self, request):
        message = request.data.get("message", {})
        text = message.get("text")
        if text == "/start":
            from_user = message.get("from", {})
            telegram_id = from_user.get("id")
            username = from_user.get("username")

            if telegram_id:
                TelegramUser.objects.get_or_create(
                    telegram_id=telegram_id,
                    defaults={"username": username}
                )

        return Response({"ok": True}, status=status.HTTP_200_OK)


class TelegramUserListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TelegramUser.objects.all().order_by('-created_at')
    serializer_class = TelegramUserSerializer
