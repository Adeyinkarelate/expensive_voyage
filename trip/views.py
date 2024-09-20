# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Trip, Itinerary, Expense
from django.contrib.auth.decorators import login_required

# Category List View


@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'categories/category_list.html', {'categories': categories})

# Category Detail View


@login_required
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk, user=request.user)
    return render(request, 'categories/category_detail.html', {'category': category})

# Category Create View


@login_required
def category_create(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        Category.objects.create(user=request.user, category_name=category_name)
        return redirect('category_list')
    return render(request, 'categories/category_create.html')


#
# Trip List View
@login_required
def trip_list(request):
    trips = Trip.objects.filter(user=request.user)
    return render(request, 'trips/trip_list.html', {'trips': trips})

# Trip Detail View


@login_required
def trip_detail(request, pk):
    trip = get_object_or_404(Trip, pk=pk, user=request.user)
    return render(request, 'trips/trip_detail.html', {'trip': trip})

# Trip Create View


@login_required
def trip_create(request):
    if request.method == 'POST':
        trip_name = request.POST.get('trip_name')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        destination = request.POST.get('destination')
        budget = request.POST.get('budget')
        currency = request.POST.get('currency')
        category = request.POST.get('category')
        Trip.objects.create(
            user=request.user,
            trip_name=trip_name,
            start_date=start_date,
            end_date=end_date,
            destination_id=destination,
            budget=budget,
            currency=currency,
            category_id=category
        )
        return redirect('trip_list')
    return render(request, 'trips/trip_create.html')


#
# Itinerary List for a Trip
@login_required
def itinerary_list(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id, user=request.user)
    itinerary_items = trip.itinerary_items.all()
    return render(request, 'itinerary/itinerary_list.html', {'trip': trip, 'itinerary_items': itinerary_items})

# Itinerary Create View


@login_required
def itinerary_create(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id, user=request.user)
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        description = request.POST.get('description')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        Itinerary.objects.create(
            trip=trip,
            title=title,
            category=category,
            description=description,
            start_time=start_time,
            end_time=end_time
        )
        return redirect('itinerary_list', trip_id=trip.pk)
    return render(request, 'itinerary/itinerary_create.html', {'trip': trip})
