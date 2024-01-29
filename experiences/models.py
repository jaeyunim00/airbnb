from django.db import models
from common.models import CommonModel

# Create your models here.


class Experience(CommonModel):

    """Experience Definition"""

    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    name = models.CharField(max_length=150)
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField("experiences.Perk")

    category = models.ForeignKey(
        "catagories.Category",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Perk(CommonModel):

    """What is included on an Experiences"""

    name = models.CharField(max_length=100)
    details = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    explanation = models.TextField()

    def __str__(self):
        return self.name
