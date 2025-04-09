from django.db import models


# Модель для хранения данных о провайдерах OAuth
# позволяет связать пользователя с аккаунтом внешнего сервиса
class OAuthProvider(models.Model):
    OAUTH_CHOICES = [
        ("yandex", "Yandex"),
        ("vk", "VK"),
    ]

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="social_accounts"
    )
    provider = models.CharField(max_length=20, choices=OAUTH_CHOICES)
    uid = models.TextField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user", "provider")

    def __str__(self):
        return f"{self.user} - {self.get_provider_display()}"
