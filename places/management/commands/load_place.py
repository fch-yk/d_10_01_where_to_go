import json
import os

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Photo, Place
from urllib.parse import urlsplit


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument(
            "-fld",
            "--folder",
            required=True,
            metavar="{folder}",
            help="folder with JSON files"
        )

    def handle(self, *args, **options):
        folder_path = options['folder']
        files_names = os.listdir(path=folder_path)
        for file_name in files_names:
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding="UTF-8") as place_file:
                place_card = json.load(place_file)

            coordinates = place_card["coordinates"]
            lng = coordinates["lng"]
            lat = coordinates["lat"]
            place, created = Place.objects.get_or_create(lng=lng, lat=lat)
            place.title = place_card["title"]
            place.description_short = place_card["description_short"]
            place.description_long = place_card["description_long"]
            place.lng = lng
            place.lat = lat
            place.save()

            if not created:
                photos = Photo.objects.filter(place=place)
                for photo in photos:
                    photo.image.delete(save=False)
                photos.delete()

            imgs = place_card["imgs"]
            for position, img_url in enumerate(imgs, start=1):
                response = requests.get(img_url)
                response.raise_for_status()
                photo = Photo(place=place, position=position)
                content = ContentFile(response.content)
                filename = urlsplit(img_url).path.split(sep='/')[-1]
                photo.image.save(filename, content, save=True)
