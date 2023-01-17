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
        img_tag = \
            "<img style='max-height: 200px; aspect-ratio: {};' src='{}'/>"
        return format_html(
            mark_safe(img_tag),
            obj.image.height // obj.image.width,
            url,
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):

    readonly_fields = ("id",)
    inlines = [PhotosInline,]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
