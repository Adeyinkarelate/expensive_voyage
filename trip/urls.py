# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Category URLs
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('categories/create/', views.category_create, name='category_create'),
    path('delete_category/<int:pk>/',views.category_delete, name='category_delete'),

    # Trip URLs
    path('trips/<int:pk>/', views.trip_detail, name='trip_detail'),
    path('trips_create/', views.trip_create, name='trip_create'),

    # Itinerary URLs
    path('trip/<int:trip_id>/create_itinerary/', views.itinerary_create, name='itinerary_create'),
    path('trip/<int:trip_id>/itinerary/', views.itinerary_list, name='itinerary_list'),
    path('update_itinerary/<int:pk>/',views.itinerary_update, name='itinerary_update'),
    path('itinerary_delete/<int:pk>/',views.itinerary_delete, name='itinerary_delete'),

    # Expense URLs
    path('expense/create/', views.expense_create, name='expense_create'),
    path('expense/', views.expense_list, name='expense_list'),
    path('expense/update/<int:pk>/', views.expense_update, name='expense_update'),
    path('expense/delete/<int:pk>/', views.expense_delete, name='expense_delete'),


]
