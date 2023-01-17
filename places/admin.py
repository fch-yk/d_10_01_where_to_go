from adminsortable2.admin import SortableTabularInline, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Photo, Place


class PhotosInline(SortableTabularInline):
    model = Photo
    readonly_fields = ("preview",)
    ordering = ("position",)
    extra = 0

    def preview(self, obj):
        url = obj.image.url
        width = obj.image.width
        height = obj.image.height
        max_height = 200
        if height > max_height:
            height = max_height
            reduction_ratio = obj.image.height / max_height
            width //= reduction_ratio

        img_tag = f"<img src='{url}' width='{width}' height={height} />"
        return format_html(mark_safe(img_tag))


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):

    readonly_fields = ("id",)
    inlines = [PhotosInline,]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ("id", "preview")

    def preview(self, obj):
        url = obj.image.url
        width = obj.image.width
        height = obj.image.height
        img_tag = f"<img src='{url}' width='{width}' height={height} />"
        return format_html(mark_safe(img_tag))
