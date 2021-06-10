from django.forms import ModelForm
from .models import Reservation, Reviews, RoomType, Room


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['room', 'check_in', 'check_out']


class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ['hotel', 'rating', 'text']
