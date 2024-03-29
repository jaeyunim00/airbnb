from django.db import models
from common.models import CommonModel


class Booking(CommonModel):

    """Booking model definition"""

    class BookingKindChoices(models.TextChoices):
        room = "room", "Room"
        experience = "experience", "Experience"

    kind = models.CharField(
        max_length=15,
        choices=BookingKindChoices.choices,
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    room = models.ForeignKey(
        "rooms.Room",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    experience = models.ForeignKey(
        "experiences.Experience",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    check_in = models.DateField(
        null=True,
        blank=True,
    )
    check_out = models.DateField(
        null=True,
        blank=True,
    )

    experience_time = models.DateTimeField(
        null=True,
        blank=True,
    )

    guests = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.kind.title()}: {self.user}"
