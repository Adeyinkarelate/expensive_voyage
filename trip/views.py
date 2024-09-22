# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Trip, Itinerary, Expense
from django.contrib.auth.decorators import login_required
from destination.models import Destination
from django.contrib import messages
from .forms import ExpenseForm, ItineraryForm

# Category List View


@login_required(login_url='login')
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'trip/category_list.html', {'categories': categories})

# Category Detail View


@login_required(login_url='login')
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk, user=request.user)
    return render(request, 'categories/category_detail.html', {'category': category})

# Category Create View


@login_required(login_url='login')
def category_create(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')

        # Check if the category already exists for this user (optional)
        if Category.objects.filter(user=request.user, category_name=category_name).exists():
            messages.error(
                request, 'You already have a category with this name.')
            return redirect('dashboard')  # or wherever you'd like to redirect

        # Create a new category and associate it with the logged-in user
        new_category = Category.objects.create(
            user=request.user,  # Link the category to the currently logged-in user
            category_name=category_name
        )

        # Optionally add a success message
        messages.success(
            request, f"Category '{new_category.category_name}' created successfully!")

        # Redirect to the category list or another page after creation
        return redirect('dashboard')

    # Render the form again if the request is GET
    return render(request, 'trip/create_category.html')


@login_required(login_url='login')  # Specify the URL name for the login page
def category_delete(request, pk):
    # Retrieve the category based on the logged-in user and category pk
    category = get_object_or_404(Category, pk=pk, user=request.user)

    if request.method == 'POST':  # Only delete on POST request to prevent accidental deletes
        category_name = category.category_name
        category.delete()  # Delete the category
        messages.success(request, f"Category '{
                         category_name}' has been deleted successfully!")
        return redirect('category_list')  # Redirect after successful deletion

    # If GET request, show a confirmation page
    return render(request, 'category/category_confirm_delete.html', {'category': category})

# =============================================================================================

# Trip Detail View


@login_required(login_url='login')
def trip_detail(request, pk):
    trip = get_object_or_404(Trip, pk=pk, user=request.user)
    return render(request, 'trip/trip_detail.html', {'trip': trip})

# Trip Create View


@login_required(login_url='login')
def trip_create(request):
    if request.method == 'POST':
        trip_name = request.POST.get('trip_name')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        destination = request.POST.get('destination')
        budget = request.POST.get('budget')
        currency = request.POST.get('currency')
        category = request.POST.get('category')

        # Create the Trip object using the form data
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
        return redirect('dashboard')  # User dashboard

    # If the request method is GET, display the form
    destinations = Destination.objects.all()  # Fetch all available destinations
    # Fetch categories for the logged-in user
    categories = Category.objects.filter(user=request.user)
    context = {
        'destinations': destinations,
        'categories': categories
    }
    return render(request, 'trip/trip_create.html', context)


# ------------------- ITINERARY VIEWS -------------------

@login_required(login_url='login')
def itinerary_create(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id, user=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        description = request.POST.get('description')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        # Ensure the correct model fields are used here
        Itinerary.objects.create(
            trip=trip,
            title=title,  # Should match the Itinerary model field
            category=category,  # Should match the Itinerary model field
            description=description,  # Should match the Itinerary model field
            start_time=start_time,  # Should match the Itinerary model field
            end_time=end_time  # Should match the Itinerary model field
        )

        return redirect('dashboard')

    return render(request, 'trip/itinerary_create.html', {'trip': trip})


@login_required(login_url='login')
def itinerary_list(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id, user=request.user)
    itineraries = Itinerary.objects.filter(trip=trip)
    context = {
        'trip': trip,
        'itineraries': itineraries
    }
    return render(request, 'trip/itinerary_list.html', context)


@login_required(login_url='login')
def itinerary_update(request, pk):
    itinerary = get_object_or_404(Itinerary, pk=pk, trip__user=request.user)
    if request.method == 'POST':
        form = ItineraryForm(request.POST, instance=itinerary)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ItineraryForm(instance=itinerary)
    return render(request, 'trip/itinerary_update.html', {'form': form})


@login_required(login_url='login')
def itinerary_delete(request, pk):
    itinerary = get_object_or_404(Itinerary, pk=pk, trip__user=request.user)
    if request.method == 'POST':
        itinerary.delete()
        messages.success(request,"You have delete the itinerary successfully")
        return redirect('dashboard')
    


# ------------------- EXPENSE VIEWS -------------------
@login_required(login_url='login')
def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expense/expense_form.html', {'form': form})


@login_required(login_url='login')
def expense_list(request):
    expenses = Expense.objects.filter(trip__user=request.user)
    return render(request, 'expense/expense_list.html', {'expenses': expenses})


@login_required(login_url='login')
def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk, trip__user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expense/expense_form.html', {'form': form})


@login_required(login_url='login')
def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk, trip__user=request.user)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expense/expense_confirm_delete.html', {'expense': expense})
