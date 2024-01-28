from django.contrib import admin
from .models import Experience, Perk

# Register your models here.


@admin.register(Experience)
class ExperienceAdmmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "start",
        "end",
        "created_at",
    )


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "details",
        "explanation",
    )