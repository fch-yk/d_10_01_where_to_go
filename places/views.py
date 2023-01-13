from django.shortcuts import render
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
