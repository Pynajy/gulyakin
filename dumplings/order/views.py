from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from order.models import (
    UserOrderHystory,
    DeliveryType,
    PymentType,
)

from lk.models import (
    Adress,
)

from market.models import ImageShop

from cart.models import (
    CartUser,
    ProductsInCart,
)

from settings.models import (
    OrderSettings,
)

from settings.tools.payment import (
    yoo_payment,
    is_payment,
)

from settings.tools.telegram import (
    # send_message_order,
    TelegramBot
)

from order.tools.geo import (
    distance_between_coordinates,
)

from settings.tools.distribution import (
    Distribution,
)

from order.tools.geo import find_nearest_addres

class CreateOrder(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        user = User.objects.get(pk=request.user.id)
        
        is_call = request.data["is_call"]
        time_delivery = request.data["time_delivery"]
        # delivery_type = DeliveryType.objects.get(pk=request.data["delivery_type"])
        delivery_type = int(request.data["delivery_type"])
        # pyment_type = PymentType.objects.get(pk=request.data["pyment_type"])
        pyment_type = int(request.data["pyment_type"])
        count_tools = int(request.data["count_tools"])


        marekt_adress_id = int(request.data["marekt_adress_id"])
        if delivery_type == 3:
            if "change_with" in request.data:
                change_with = int(request.data["change_with"])
            adress_id = 21
        else:
            change_with = 0
            # marekt_adress_id = 12
            adress_id = request.data["user_adress_id"]


        # Получаем существующий объект CartUser
        cart_user = CartUser.objects.get(user=user)

        # Создаем новый объект UserOrderHystory на основе данных из CartUser и передаем адресный идентификатор
        order = UserOrderHystory.create_order_from_cart_user(cart_user=cart_user, 
                                                             adress_id=adress_id, 
                                                             is_call=is_call, 
                                                             delivery_type=delivery_type, 
                                                             pyment_type=pyment_type,
                                                             time_delivery=time_delivery,
                                                             market_adress_id=marekt_adress_id,
                                                             count_tools=count_tools
                                                             )
        if isinstance(order, UserOrderHystory):

            # Сохраняем новый объект в базе данных
            if order.pyment_type.pk == 1:
                payment = yoo_payment(order.price, order.pk, user.username)
                order.pyment_id = payment.id
                order.save()

            cart_user.products.clear()
            cart_user.save()

            if order.pyment_type.pk == 1:
                th = TelegramBot(order.pk)
                th.start()
                return Response({"status": True, "order_id": order.pk, "payment": True, "payment_url": payment.confirmation.confirmation_url})
            else:
                th = TelegramBot(order.pk)
                th.start()
                return Response({"status": True, "order_id": order.pk, "payment": False})

        else:
            return Response(order, status=status.HTTP_400_BAD_REQUEST)


class GetOrder(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = User.objects.get(pk=request.user.id)

        order_id = request.query_params.get("order_id")

        user_order = UserOrderHystory.objects.filter(pk=order_id).first()

        order_data = {
            "order_id": user_order.pk,
            "datetime": user_order.datetime,
            "price": int(user_order.price),
            "is_payment": user_order.is_pyment,
            "is_active": user_order.is_activ,
            "products": [{
                "id": product.id,
                "price": product.product.price,
                "price_discount": product.product.price - ((product.product.price / 100) * user_order.discount),
                "title": product.product.title,
                "image": f"/media/{product.product.image}",
                } for product in user_order.products.all()],
            "address": str(user_order.adress),
        }

        return Response({"status": True, "order": order_data})


class ListOrder(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = User.objects.filter(pk=request.user.id).first()
        user_order = UserOrderHystory.objects.filter(user=user)
        order_data = [{
            "order_id": i.pk,
            "datetime": i.datetime,
            "price": i.price,
            "is_payment": i.is_pyment,
            "is_active": i.is_activ,
            "address": str(i.adress),
            "products": [{
                "id": (product.product.pk if not product.is_combo else product.combo.combo.pk),
                "price": product.product.price,
                "title": str(product),
                "image": (f"/media/{product.product.image}" if not product.is_combo else f"/media/{product.combo.combo.image}"),
                } for product in i.products.all()],
        } for i in user_order]

        return Response({"status": True, "order": order_data})


class OrderPaymentSuccess(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        order_id = request.data["order_id"]
        order = UserOrderHystory.objects.get(pk=order_id)
        if is_payment(order.pyment_id):
            order.is_pyment = True
            order.save()
            return Response({"status": True})
        else:
            return Response({"status": False, "error": "Not_paid"}, status=status.HTTP_402_PAYMENT_REQUIRED)
        

class GetDeliveryType(APIView):
    def get(self, request):
        delivery_type = DeliveryType.objects.all()
        delivery = [{
            "id": i.pk,
            "title": i.title
        } for i in delivery_type]

        return Response({"status": True, "delivery_list": delivery})


class GetPaymentType(APIView):
    def get(self, request):
        payment_type = PymentType.objects.all()
        payment = [{
            "id": i.pk,
            "title": i.title
        } for i in payment_type]

        return Response({"status": True, "payment_list": payment})


class GetTypeDeliveryForCoord(APIView):
    permission_classes = (IsAuthenticated, )
    
    def get(self, request):
        lat = request.query_params.get("lat")
        lon = request.query_params.get("lon")
        siti = request.query_params.get("siti_id")

        distribution = Distribution(request.user.id, lon, lat)
        resp = distribution.nearest_adresses(siti)

        order_settings = OrderSettings.objects.first()
        
        if not resp:
            return Response({"status": True, "delivery_type": 2, "price": order_settings.people_price_delivery}) 

        distance_m = distance_between_coordinates(float(lat), float(lon), resp.lat, resp.long)

        if order_settings.people_long_delivery >= distance_m:
            return Response({"status": True, "delivery_type": 1, "price": order_settings.people_price_delivery})
        else:
            return Response({"status": True, "delivery_type": 2, "price": order_settings.auto_price_delivery})


class CheckMultiCart(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        distribution = Distribution(request.user.id)
        resp = distribution.check_true_order(request.query_params.get("siti_id"))

        return Response(resp)


class GetAdressForPickup(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        cart = CartUser.objects.get(user=request.user.id)
        if cart.products.count() != 0:
            distribution = Distribution(request.user.id)
            resp = distribution.check_true_order(request.query_params.get("siti_id"), get_adress=True)

            list_id_adress = [i["market_id"] for i in resp["adress"]]
            print(list_id_adress)

            adress_id = request.query_params.get("adress_id")
            if adress_id:
                adress = Adress.objects.get(pk=adress_id)
                nearest_delivery_point = find_nearest_addres(
                    adress.long, 
                    adress.lat, 
                    is_list_adress=True, 
                    list_id=list_id_adress, 
                    siti_id=request.query_params.get("siti_id"))
                
                if nearest_delivery_point:
                    image_shop = ImageShop.objects.filter(shop=nearest_delivery_point)
                    data = {
                        "id": nearest_delivery_point.pk, 
                        "adress": nearest_delivery_point.adress, 
                        "market": {
                            "id": nearest_delivery_point.shop.pk,
                            "name": nearest_delivery_point.shop.name,
                            "short_description": nearest_delivery_point.shop.short_description,
                            "description": nearest_delivery_point.shop.description,
                            "link": nearest_delivery_point.shop.link,
                        }, 
                        "lat": nearest_delivery_point.long, 
                        "long": nearest_delivery_point.lat,
                        "is_around_clock": nearest_delivery_point.is_around_clock,

                        "time": [
                            [nearest_delivery_point.monday_with, nearest_delivery_point.monday_until],
                            [nearest_delivery_point.tuesday_with, nearest_delivery_point.tuesday_until],
                            [nearest_delivery_point.wednesday_with, nearest_delivery_point.wednesday_until],
                            [nearest_delivery_point.thursday_with, nearest_delivery_point.thursday_until],
                            [nearest_delivery_point.friday_with, nearest_delivery_point.friday_until],
                            [nearest_delivery_point.saturday_with, nearest_delivery_point.saturday_until],
                            [nearest_delivery_point.sunday_with, nearest_delivery_point.sunday_until],
                        ],
                        "phone": nearest_delivery_point.phone,
                        "timeaone": f"{nearest_delivery_point.timezone}",
                        "image": [f"/media/{i.image}" for i in image_shop],
                    }
                    resp["delivery_adress"] = data

            return Response(resp)
        else:
            return Response({"status": False, "error": "cart_is_clear"})