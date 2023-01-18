from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Place
from django.urls import reverse


def show_home(request):

    features = []
    for place in Place.objects.all():
        feature = {
            "type": "Feature",
            "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse(place_details, args=[place.id]),
            }
        }
        features.append(feature)

    places = {
        "type": "FeatureCollection",
        "features": features,
    }

    return render(request, 'index.html', context={"places": places})


def place_details(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    imgs = []

    photos = place.photos.all()
    imgs = [
        request.build_absolute_uri(photo.image.url) for photo in photos
    ]

    place_card = {
        "title": place.title,
        "imgs": imgs,
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        },
    }

    return JsonResponse(
        place_card,
        json_dumps_params={"ensure_ascii": False, "indent": 4}
    )
