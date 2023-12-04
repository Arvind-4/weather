import re
from django.views import View
from django.core.cache import cache
from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse

from .forms import WeatherForm
from .data import get_weather_data
from .utils import set_cities_data, get_clean_city_name


# Create your views here.


class HomePageView(View):
    context: dict = {}

    def get(self, request: HttpRequest, *args, **kwargs):
        form = WeatherForm()
        self.context["form"] = form
        return render(request, "index.html", context=self.context)

    def post(self, request: HttpRequest, *args, **kwargs):
        form = WeatherForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            return redirect(f"/p/{get_clean_city_name(name)}")
        self.context["form"] = form
        return render(request, "index.html", context=self.context)


class CityPageView(View):
    context: dict = {}

    def get(self, request: HttpRequest, *args, **kwargs):
        name = kwargs.get("name")
        data = get_weather_data(name)
        if data:
            self.context["data"] = data
            return render(request, "info.html", context=self.context)
        else:
            return render(request, "error.html", context=self.context)


class CityAutoCompleteView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        query = request.GET.get("term", None)
        if query is None:
            return JsonResponse({}, safe=False)
        if cache.get("cities") is None:
            cities = set_cities_data()
            print("Lastest data from csv file")
        else:
            cities = cache.get("cities")
            print("Cached data")
        results = [city for city in cities if re.search(query, city, re.IGNORECASE)][:8]
        return JsonResponse(results, safe=False)
