from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
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
    return HttpResponse(place.title)
