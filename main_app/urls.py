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
    path('restaurants/<int:restaurant_id>/add_review/', views.add_review, name='add_review'),
    path('restaurants/<int:pk>/delete_review/', views.DeleteReview.as_view(), name='delete_review'),
    path('restaurant/<int:restaurant_id>/add_day', views.add_day, name='add_day'),
    path('restaurant/<int:restaurant_id>/add_photo', views.add_photo, name='add_photo'),
    path('days/create/<int:restaurant_id>/', views.DayCreate.as_view(), name='days_create'),
    path('days/detail/<int:pk>/', views.DayDetail.as_view(), name='days_detail'),
    path('days/<int:pk>/update/', views.DayUpdate.as_view(), name='days_update'),
    path('days/<int:pk>/delete/', views.DayDelete.as_view(), name='days_delete'),
]
