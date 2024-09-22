# models.py
from django.db import models
from account.models import User
# Assuming this model is already defined
from destination.models import Destination


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    destination = models.ForeignKey(Destination, on_delete=models.SET_NULL, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.trip_name} to {self.destination.name}"


class Itinerary(models.Model):
    CATEGORY_CHOICES = [
        ('transport', 'Transport'),
        ('lodging', 'Lodging'),
        ('activities', 'Activities'),
    ]

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='itinerary_items')
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.title} ({self.category})"

    
class Expense(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    expense_date = models.DateField()
    notes = models.TextField(blank=True)
    currency = models.CharField(max_length=3, default='USD')  # Support multiple currencies

    def __str__(self):
        return f"{self.category} - {self.amount}"


class Budget(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='budgets')
    total_budget = models.DecimalField(max_digits=10, decimal_places=2)
    category_budget = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Budget for {self.trip.trip_name}"