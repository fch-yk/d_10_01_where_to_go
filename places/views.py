from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Place


def home(request):

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
                "detailsUrl": "./static/places/moscow_legends.json",  # FIXME
            }
        }
        features.append(feature)

    # FIXME debug
    features[1]["properties"]["detailsUrl"] = "./static/places/roofs24.json"

    places = {
        "type": "FeatureCollection",
        "features": features,
    }

    context = {"places": places}
    return render(request, 'index.html', context=context)


def place_details(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    imgs = []
    for photo in place.photos.all():
        absolute_uri = request.build_absolute_uri(photo.image.url)
        imgs.append(absolute_uri)

    place_card = {
        "title": place.title,
        "imgs": imgs,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        },
    }

    dumps_params = {"ensure_ascii": False, "indent": 4}
    return JsonResponse(place_card, json_dumps_params=dumps_params)
