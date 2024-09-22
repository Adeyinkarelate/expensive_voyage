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
        fields = ['trip_name', 'start_date', 'end_date','destination', 'budget', 'currency', 'category']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


# Form for Itinerary model
class ItineraryForm(forms.ModelForm):
    class Meta:
        model = Itinerary
        fields = ['title', 'category', 'description', 'start_time', 'end_time']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'start_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

# Form for Expense model
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['item', 'cost', 'currency']
        widgets = {
            'item': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter item name'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter cost'}),
            'currency': forms.Select(attrs={'class': 'form-control'}),
        }