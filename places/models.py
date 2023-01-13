from django.db import models


class Place(models.Model):
    title = models.CharField("Title", max_length=200)
    description_short = models.TextField("Short description")
    description_long = models.TextField("Long description")
    lng = models.FloatField("longitude")
    lat = models.FloatField("latitude")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Photo(models.Model):
    image = models.ImageField("Image", upload_to="images")
    position = models.SmallIntegerField("Position")
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
