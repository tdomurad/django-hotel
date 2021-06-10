from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *


def home(request):
    context = {
        'hotels': Hotel.objects.all(),
        'room_types': RoomType.objects.all(),
    }
    return render(request, 'hotel/home.html', context)


def create_review(request):
    form = ReviewsForm
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.guest = request.user
            review.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'hotel/review_form.html', context)


def reservation_list(request):
    context = {
        'reservations': Reservation.objects.all(),
        'hotels': Hotel.objects.all(),
        'room_types': RoomType.objects.all(),
        'room': Room.objects.all()
    }
    return render(request, 'hotel/reservation_list.html', context)


def create_reservation(request):
    form = ReservationForm
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.guest = request.user
            reservation.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'hotel/reservation_form.html', context)


class HotelDetailView(DetailView):
    model = Hotel
    context_object_name = 'hotel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room_types'] = RoomType.objects.all()
        context['rooms'] = Room.objects.all()
        context['reviews'] = Reviews.objects.all()
        return context


class HotelCreateView(CreateView):
    model = Hotel
    fields = ['name', 'description', 'stars', 'address', 'image']


class HotelUpdateView(UpdateView):
    model = Hotel
    fields = ['name', 'description', 'stars', 'address', 'image']


class HotelDeleteView(DeleteView):
    model = Hotel
    success_url = '/'


def about(request):
    return render(request, 'hotel/about.html', {'title': 'About'})
