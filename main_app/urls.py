from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('users/signup/', views.signup, name='signup'),
    path('restaurants/', views.restaurants_index, name='index'),
    path('restaurants/<int:restaurant_id>/', views.restaurants_detail, name='detail'),
    path('restaurants/create/', views.RestaurantCreate.as_view(), name='restaurants_create'),
    path('restaurants/<int:restaurant_id>/update/', views.RestaurantUpdate.as_view(), name='restaurants_update')
]