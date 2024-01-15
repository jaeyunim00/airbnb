from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("femail", "Femail")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        WON = ("won", "Korean Won")
        USD = ("usd", "Dollar")

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    name = models.CharField(
        max_length=150,
        default="",
    )
    is_host = models.BooleanField(
        default=False,
    )
    avatar = models.ImageField(blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
        null=True,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
        null=True,
    )
    currency = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
        null=True,
    )
