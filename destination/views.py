from django.shortcuts import render, get_object_or_404
from .models import Destination


def destination_list(request):
    # Get the search query from the request
    search_query = request.GET.get('search', '')
    # Get the filter by country from the request
    filter_country = request.GET.get('country', '')

    # Fetch destinations based on search and filter conditions
    destinations = Destination.objects.all()

    # If there is a search query, filter destinations by name
    if search_query:
        destinations = destinations.filter(name__icontains=search_query)

    # If there is a filter by country, filter destinations by country
    if filter_country:
        destinations = destinations.filter(country__icontains=filter_country)

    # Get all unique countries for the filter dropdown
    countries = Destination.objects.values_list(
        'country', flat=True).distinct()

    context = {
        'destinations': destinations,
        'search_query': search_query,
        'filter_country': filter_country,
        'countries': countries,
    }

    return render(request, 'destination/destination_list.html', context)

# views.py


def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    return render(request, 'destination/destination_detail.html', {'destination': destination})
