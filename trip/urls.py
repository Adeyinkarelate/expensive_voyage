# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Category URLs
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('categories/create/', views.category_create, name='category_create'),
    
    # Trip URLs
    path('trips/', views.trip_list, name='trip_list'),
    path('trips/<int:pk>/', views.trip_detail, name='trip_detail'),
    path('trips/create/', views.trip_create, name='trip_create'),

    # Itinerary URLs
    path('trips/<int:trip_id>/itinerary/', views.itinerary_list, name='itinerary_list'),
    path('trips/<int:trip_id>/itinerary/create/', views.itinerary_create, name='itinerary_create'),

    # Expense URLs
    path('trips/<int:trip_id>/expenses/', views.expense_list, name='expense_list'),
    path('trips/<int:trip_id>/expenses/create/', views.expense_create, name='expense_create'),
]
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Category URLs
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('categories/create/', views.category_create, name='category_create'),
    
    # Trip URLs
    path('trips/', views.trip_list, name='trip_list'),
    path('trips/<int:pk>/', views.trip_detail, name='trip_detail'),
    path('trips/create/', views.trip_create, name='trip_create'),

    # Itinerary URLs
    path('trips/<int:trip_id>/itinerary/', views.itinerary_list, name='itinerary_list'),
    path('trips/<int:trip_id>/itinerary/create/', views.itinerary_create, name='itinerary_create'),

    # Expense URLs
    path('trips/<int:trip_id>/expenses/', views.expense_list, name='expense_list'),
    path('trips/<int:trip_id>/expenses/create/', views.expense_create, name='expense_create'),
]
