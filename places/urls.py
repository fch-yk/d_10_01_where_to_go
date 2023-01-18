from django.urls import path

from places import views

urlpatterns = [
    path('', views.show_home),
    path('places/<int:place_id>/', views.place_details),
]
