from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('register/', views.register, name='register'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('profile/<int:pk>/', views.profile_details, name='profile_details'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
]
