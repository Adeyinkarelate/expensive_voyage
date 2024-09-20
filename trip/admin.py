# admin.py
from django.contrib import admin
from .models import Category, Trip, Itinerary, Expense  # Adjust the import path according to your project structure

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'user')
    search_fields = ('category_name', 'user__username')

class TripAdmin(admin.ModelAdmin):
    list_display = ('trip_name', 'user', 'start_date', 'end_date', 'destination', 'budget', 'currency', 'category')
    list_filter = ('start_date', 'end_date', 'user', 'destination', 'category')
    search_fields = ('trip_name', 'destination__name', 'category__category_name', 'user__username')

class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('title', 'trip', 'category', 'start_time', 'end_time')
    list_filter = ('category', 'start_time', 'end_time')
    search_fields = ('title', 'trip__trip_name')

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('trip', 'amount', 'category', 'expense_date')
    list_filter = ('expense_date', 'category')
    search_fields = ('trip__trip_name', 'category')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Trip, TripAdmin)
admin.site.register(Itinerary, ItineraryAdmin)
admin.site.register(Expense, ExpenseAdmin)
