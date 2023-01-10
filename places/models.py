from django.db import models


class Place(models.Model):
    title = models.CharField("Title", max_length=200)
    description_short = models.TextField("Short description")
    description_long = models.TextField("Long description")
    lng = models.FloatField("longitude")
    lat = models.FloatField("latitude")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
