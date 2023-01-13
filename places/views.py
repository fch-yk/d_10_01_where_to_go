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
                "detailsUrl": "./static/places/moscow_legends.json"
            }
        }
        features.append(feature)

    places = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [37.62, 55.793676]
                },
                "properties": {
                    "title": "«Легенды Москвы",
                    "placeId": "moscow_legends",
                    "detailsUrl": "./static/places/moscow_legends.json"
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [37.64, 55.753676]
                },
                "properties": {
                    "title": "Крыши24.рф",
                    "placeId": "roofs24",
                    "detailsUrl": "./static/places/roofs24.json"
                }
            }
        ]
    }

    context = {"places": places}
    return render(request, 'index.html', context=context)
