from django.urls import path
from .views import HomePageView, CityPageView, CityAutoCompleteView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("p/<str:name>/", CityPageView.as_view(), name="city"),
    path("api/autocomplete/", CityAutoCompleteView.as_view(), name="autocomplete"),
]
