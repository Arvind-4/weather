from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .data import get_weather_data
from .forms import WeatherForm

# Create your views here.


def index(request):
    if request.method == "POST":
        form = WeatherForm(request.POST)
        if form.is_valid():
            name = request.POST["name"]
            return redirect(f"/{name}")

    form = WeatherForm()
    context = {
        "form": form,
    }
    return render(request, "index.html", context=context)


def information(request, name):
    data = get_weather_data(name)
    if data:
        context = {
            "data": data,
        }
        return render(request, "info.html", context=context)
    else:
        return render(request, "error.html", {})


# def error_view(request):
# 	return render(request, 'error.html', context={})
