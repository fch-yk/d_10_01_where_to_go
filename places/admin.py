from django.contrib import admin
from .models import Place, Photo


class PhotosInline(admin.TabularInline):
    model = Photo


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
    inlines = [PhotosInline,]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
