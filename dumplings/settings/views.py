from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from settings.models import (
    ErrorClient,
)

from settings.models import (
    OrderSettings,
    GlobalSettings,
)

from settings.tools.distribution import Distribution

class GetErrorInClient(APIView):
    def post(self, request):
        datetime = request.data["datetime"]
        sent_data = request.data["sent_data"]
        received_response = request.data["received_response"]
        status = request.data["status"]
        user = request.data["user"]
        url = request.data["url"]

        error_client = ErrorClient.objects.create(
            datetime=datetime,
            sent_data=sent_data,
            received_response=received_response,
            status=status,
            user=user,
            url=url
        )
        
        return Response({"status": True})


class TestDistribution(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        distribution = Distribution(request.user.id)

        return Response(distribution.check_multi_shop())


class GetOrderSettings(APIView):
    def get(self, request):
        order_settings = OrderSettings.objects.last()

        data = {
            "status": True,
            "car_min": order_settings.min_prise_auto,
            "people_min": order_settings.people_price_delivery

        }

        return Response(data)


class GetGlobalSettings(APIView):
    def get(self, request):
        gs = GlobalSettings.objects.last()
        data = {
            "is_dev": gs.is_dev,
            "is_disabled_cart": gs.is_disabled_cart,
            "is_disabled_online_pyment": gs.is_disabled_online_pyment,
            "is_disabled_cash_pyment": gs.is_disabled_cash_pyment,
            "is_disabled_auto_delivery": gs.is_disabled_auto_delivery,
            "is_disabled_people_delivery": gs.is_disabled_people_delivery,
            "is_disabled_pickup_delivery": gs.is_disabled_pickup_delivery,
            "is_disabled_reservation": gs.is_disabled_reservation,
            "is_disabled_order": gs.is_disabled_order
        }

        return Response(data)