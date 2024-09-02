from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        station_reader = csv.DictReader(csvfile)
        stations_list = [row for row in station_reader]

        paginator = Paginator(stations_list, 10)

        request_page = request.GET.get('page', 1)
        page = paginator.get_page(request_page)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
