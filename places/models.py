from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField("Title", max_length=200)
    short_description = models.TextField("Short description", blank=True)
    long_description = HTMLField("Long description", blank=True)
    lng = models.FloatField("longitude")
    lat = models.FloatField("latitude")

    class Meta:
        ordering = ["title"]
        unique_together = ["lng", "lat"]

    def __str__(self):
        return self.title


class Photo(models.Model):
    image = models.ImageField("Image", upload_to="images")
    position = models.PositiveSmallIntegerField(
        verbose_name="Position",
        default=0,
        db_index=True,
    )
    place = models.ForeignKey(
        "Place",
        verbose_name="Place",
        on_delete=models.CASCADE,
        related_name="photos",
    )

    class Meta:
        ordering = ["place__title", "position"]

    def __str__(self):
        return f"{self.place.title} photo {self.position}"
