from django.urls import path, include

from booking.views import (
    ListBookingView,
    CreateBooking,
)

urlpatterns = [
    path('create', CreateBooking.as_view(), name='CreateBooking'),
    path('list', ListBookingView.as_view(), name='ListBookingView'),
]