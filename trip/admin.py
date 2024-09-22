# admin.py
from django.contrib import admin
# Adjust the import path according to your project structure
from .models import Category, Trip, Itinerary, Expense


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'user')
    search_fields = ('category_name', 'user__username')


class TripAdmin(admin.ModelAdmin):
    list_display = ('trip_name', 'user', 'start_date', 'end_date',
                    'destination', 'budget', 'currency', 'category')
    list_filter = ('start_date', 'end_date', 'user', 'destination', 'category')
    search_fields = ('trip_name', 'destination__name',
                     'category__category_name', 'user__username')


@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ['trip', 'title', 'category', 'start_time', 'end_time']
    search_fields = ['title', 'category', 'trip__trip_name']
    list_filter = ['category', 'start_time', 'end_time']
    ordering = ['start_time']
    list_per_page = 20

# Expense Admin


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['trip', 'item', 'cost', 'currency']
    search_fields = ['item', 'trip__trip_name']
    list_filter = ['currency']
    ordering = ['trip', 'cost']
    list_per_page = 20


admin.site.register(Category, CategoryAdmin)
admin.site.register(Trip, TripAdmin)

