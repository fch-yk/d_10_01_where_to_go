from django.contrib import admin
from .models import Place, Photo


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
