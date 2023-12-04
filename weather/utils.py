import csv
from django.conf import settings
from django.core.cache import cache
from django.utils.text import slugify

ONE_DAY = 60 * 60 * 24
ONE_WEEK = ONE_DAY * 7

CSV_DIR = settings.BASE_DIR / "data"
CSV_FILE = CSV_DIR / "worldcities.csv"


def set_cities_data():
    with open(CSV_FILE) as f:
        reader = csv.reader(f)
        data = sorted(list(reader))
    try:
        cities = [str(row[1]) for row in data]
        cache.set("cities", cities, timeout=ONE_WEEK)
        print("Successfully cached data")
        return cities
    except Exception as e:
        print("Error while caching data", e)
        return None


def get_clean_city_name(city: str) -> str:
    return slugify(city.strip().lower())
