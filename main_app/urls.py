from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('users/signup/', views.signup, name='signup'),
    path('restaurants/', views.restaurants_index, name='index'),
    path('restaurants/<int:restaurant_id>/', views.restaurants_detail, name='detail'),
    path('restaurants/create/', views.RestaurantCreate.as_view(), name='restaurants_create'),
    path('restaurants/<int:pk>/update/', views.RestaurantUpdate.as_view(), name='restaurants_update'),
    path('restaurants/<int:pk>/delete', views.RestaurantDelete.as_view(), name='restaurants_delete'),
    path('restaurants/<int:restaurant_id>/assoc_day/<int:day_id>', views.assoc_day, name='assoc_day'),
    path('restaurants/<int:restaurant_id>/unassoc_day/<int:day_id>', views.unassoc_day, name='unassoc_day'),
]
