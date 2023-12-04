from django.shortcuts import render


def handler404(request, exception, *args, **kwargs):
    return render(request, "error.html", {}, status=404)
