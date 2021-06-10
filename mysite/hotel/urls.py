from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.home, name='hotel-home'),
    path('review/', views.create_review, name='hotel-review'),
    path('reservation_form/', views.create_reservation, name='hotel-book'),
    path('reservations/', views.reservation_list, name='hotel-reservations'),
    path('hotel/<int:pk>/', HotelDetailView.as_view(), name='hotel-detail'),
    path('hotel/new/', HotelCreateView.as_view(), name='hotel-create'),
    path('hotel/<int:pk>/update/', HotelUpdateView.as_view(), name='hotel-update'),
    path('hotel/<int:pk>/delete/', HotelDeleteView.as_view(), name='hotel-delete'),
    path('about/', views.about, name='hotel-about'),
]