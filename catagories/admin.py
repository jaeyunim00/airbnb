from django.contrib import admin
from .models import Category


@admin.register(Category)
class CatagoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "kind",
    )

    list_filter = ("kind",)
