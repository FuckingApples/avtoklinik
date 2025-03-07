from django.contrib.auth.hashers import check_password
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Менеджер пользователей с методами создания обычного пользователя и суперпользователя
# При создании суперпользователя устанавливаются флаги is_staff и is_superuser
class UserManager(BaseUserManager):
    def create_user(
        self, email, first_name, last_name, password=None, **extra_fields
    ) -> "User":
        if not email:
            raise ValueError("Users must have an email address")
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, first_name, last_name, password=None, **extra_fields
    ) -> "User":
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        user = self.create_user(email, first_name, last_name, password, **extra_fields)
        user.save()
        return user


# Модель пользователя с расширенным полем email и убранным полем username
# Поле email уникально и используется в качестве логина
# Поле organizations - связь с моделью организаций
class User(AbstractUser):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField(max_length=255, unique=True)
    is_email_verified = models.BooleanField(default=False)
    password = models.TextField()
    organizations = models.ManyToManyField(
        "organizations.Organization",
        blank=True,
        through="organizations.Membership",
        related_name="users",
    )

    username = None

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Модель для хранения OTP-кодов пользователей для подтверждения email
# Поле otp_secret - хэш-код OTP-кода
# Поле is_verified - флаг использования OTP-кода
# Поле lifetime - время жизни OTP-кода в секундах по умолчанию 12 часов
class UserOTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp_secret = models.CharField(max_length=32, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    lifetime = models.IntegerField(default=60 * 60 * 12)
    is_verified = models.BooleanField(default=False)

    # Проверка на истечение времени жизни OTP-кода
    def is_expired(self):
        from django.utils.timezone import now

        return (now() - self.created_at).total_seconds() > self.lifetime

    #    def save(self, *args, **kwargs):
    #        if not self.pk or not self.otp_secret.startswith("pbkdf2_"):
    #            self.otp_secret = make_password(self.otp_secret)
    #        super().save(*args, **kwargs)

    def verify_otp_secret(self, raw_otp_secret):
        return check_password(raw_otp_secret, self.otp_secret)
