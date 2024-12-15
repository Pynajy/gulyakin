from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

from booking.models import (
    BookingModel,
    ListBooing,
)


class ListBookingView(APIView):
    def get(self, request):
        siti_id = request.query_params.get("siti_id")
        return Response({"status": True, "booking": [{
            "id": i.adress.pk,
            "adress": i.adress.adress,
            "link": i.adress.shop.link,
            "lat": i.adress.lat,
            "long": i.adress.long,
            "time": [
                [i.adress.monday_with, i.adress.monday_until],
                [i.adress.tuesday_with, i.adress.tuesday_until],
                [i.adress.wednesday_with, i.adress.wednesday_until],
                [i.adress.thursday_with, i.adress.thursday_until],
                [i.adress.friday_with, i.adress.friday_until],
                [i.adress.saturday_with, i.adress.saturday_until],
                [i.adress.sunday_with, i.adress.sunday_until],
            ],
            } for i in ListBooing.objects.filter(siti=siti_id)]})


class CreateBooking(APIView):
    def post(self, request):
        adress = request.data["adress"]
        date = request.data["date"]
        time = request.data["time"]
        count_guest = request.data["count_guest"]
        name = request.data["name"]
        phone = request.data["phone"]

        booking_model = BookingModel.objects.create(
            adress = ListBooing.objects.filter(adress=adress).first(),
            time = time,
            count_guest = count_guest,
            name = name,
            phone = phone
        )

        return Response({"status": True})