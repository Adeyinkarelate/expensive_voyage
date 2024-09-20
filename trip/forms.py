# forms.py
from django import forms
from .models import Category, Trip, Itinerary, Expense

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['trip_name', 'start_date', 'end_date', 'destination', 'budget', 'currency', 'category']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ItineraryForm(forms.ModelForm):
    class Meta:
        model = Itinerary
        fields = ['title', 'category', 'description', 'start_time', 'end_time']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'category', 'expense_date', 'notes']
        widgets = {
            'expense_date': forms.DateInput(attrs={'type': 'date'}),
        }
