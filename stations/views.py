import csv
from pagination.settings import BUS_STATION_CSV
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse


with open(BUS_STATION_CSV, encoding='utf-8') as file:
    reader = csv.DictReader(file)
    BUS_STATION_LIST = []
    for station in reader:
        BUS_STATION_LIST.append({
            'Name': station['Name'],
            'Street': station['Street'],
            'District': station['District']
        })


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(BUS_STATION_LIST, 8)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
