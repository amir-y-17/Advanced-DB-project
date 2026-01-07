from django.urls import path
from . import views


app_name = "locations"
urlpatterns = [
    path(
        "provinces/",
        views.ProvinceListCreateView.as_view(),
        name="province-list-create",
    ),
    path(
        "provinces/<int:pk>/",
        views.ProvinceDeleteView.as_view(),
        name="province-delete",
    ),
    path("cities/", views.CityListCreateView.as_view(), name="city-list-create"),
    path("cities/<int:pk>/", views.CityDeleteView.as_view(), name="city-delete"),
    path(
        "villages/", views.VillageListCreateView.as_view(), name="village-list-create"
    ),
    path(
        "villages/<int:pk>/", views.VillageDeleteView.as_view(), name="village-delete"
    ),
]
