from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

from market.models import (
    Siti,
    Shop,
    Adress,
    ImageShop,
)

from product.models import Products

class GetMarketInSiti(APIView):
    def get(self, request):
        siti_id = request.query_params.get("siti_id")
        adress = Adress.objects.filter(siti=siti_id)

        unique_links = set()
        unique_market_list = []

        is_foodholl = False

        for i in adress:
            if i.shop.link == 1:
                is_foodholl = True
                break
            link = i.shop.link
            if link not in unique_links:
                unique_links.add(link)
                market_data = {
                    "id": i.shop.pk,
                    "link": link,
                    "market": i.shop.name,
                }
                unique_market_list.append(market_data)
        if is_foodholl:
            for i in Shop.objects.all():
                unique_market_list.append({
                    "id": i.pk,
                    "link": i.link,
                    "market": i.name,
                })

        return Response({"status": True, "market": unique_market_list})



class GetSiti(APIView):
    def get(self, request):
        siti = [{"id": i.pk, "name": i.name} for i in Siti.objects.all()]
        return Response({"status": True, "siti": siti})


# class GetAdress(APIView):
#     def get(self, request):
#         siti_id = request.query_params.get("siti_id")
#         adress = [{
#             "id": i.pk, 
#             "siti": i.siti.name,
#             "market_id": i.shop.pk, 
#             "market": i.shop.name,
#             "adress": i.adress, 
#             "lat": i.long, 
#             "long": i.lat,
#             "phone": i.phone,
#             "time": [
#                 [i.monday_with, i.monday_until],
#                 [i.tuesday_with, i.tuesday_until],
#                 [i.wednesday_with, i.wednesday_until],
#                 [i.thursday_with, i.thursday_until],
#                 [i.friday_with, i.friday_until],
#                 [i.saturday_with, i.saturday_until],
#                 [i.sunday_with, i.sunday_until],
#             ],
#             "is_around_clock": i.is_around_clock,

#             # "monday_with": i.monday_with,
#             # "monday_until": i.monday_until,

#             # "tuesday_with": i.tuesday_with,
#             # "tuesday_until": i.tuesday_until,

#             # "wednesday_with": i.wednesday_with,
#             # "wednesday_until": i.wednesday_until,

#             # "thursday_with": i.thursday_with,
#             # "thursday_until": i.thursday_until,

#             # "friday_with": i.friday_with,
#             # "friday_until": i.friday_until,

#             # "saturday_with": i.saturday_with,
#             # "saturday_until": i.saturday_until,

#             # "sunday_with": i.sunday_with,
#             # "sunday_until": i.sunday_until,
#             } for i in Adress.objects.filter(siti=siti_id)]
#         return Response({"status": True, "adress": adress})


class GetAdress(APIView):
    def get(self, request):
        siti_id = request.query_params.get("siti_id")
        unique_addresses = set()  # Множество для хранения уникальных адресов
        adress = []

        for i in Adress.objects.filter(siti=siti_id):
            if i.adress not in unique_addresses:
                unique_addresses.add(i.adress)
                adress.append({
                    "id": i.pk,
                    "siti": i.siti.name,
                    "market_id": i.shop.pk,
                    "market": i.shop.name,
                    "adress": i.adress,
                    "lat": i.long,
                    "long": i.lat,
                    "phone": i.phone,
                    "time": [
                        [i.monday_with, i.monday_until],
                        [i.tuesday_with, i.tuesday_until],
                        [i.wednesday_with, i.wednesday_until],
                        [i.thursday_with, i.thursday_until],
                        [i.friday_with, i.friday_until],
                        [i.saturday_with, i.saturday_until],
                        [i.sunday_with, i.sunday_until],
                    ],
                    "is_around_clock": i.is_around_clock,
                })

        return Response({"status": True, "adress": adress})



class GetMarketAdressInSiti(APIView):
    def get(self, request):
        market_id = request.query_params.get("market_id")
        siti_id = request.query_params.get("siti_id")
        adress = Adress.objects.filter(siti=siti_id, shop=market_id)
        adress = [{
            "id": i.pk, 
            "adress": i.adress, 
            "market_id": i.shop.pk, 
            "market": i.shop.name, 
            "lat": i.long, 
            "long": i.lat,
            "phone": i.phone, 
            "is_around_clock": i.is_around_clock,

            "time": [
                [i.monday_with, i.monday_until],
                [i.tuesday_with, i.tuesday_until],
                [i.wednesday_with, i.wednesday_until],
                [i.thursday_with, i.thursday_until],
                [i.friday_with, i.friday_until],
                [i.saturday_with, i.saturday_until],
                [i.sunday_with, i.sunday_until],
            ],
            } for i in adress]
        return Response({"status": True, "adress": adress})  


class GetMarketInfo(APIView):
    def get(self, request):
        market = Shop.objects.get(pk=request.query_params.get("market_id"))
        if market:
            shop = {
                "id": market.pk,
                "name": market.name,
                "short_description": market.short_description,
                "description": market.description,
                "link": market.link,
            }
            return Response({"status": True, "shop": shop})
        else:
            return Response({"status": False, "error": "market_not_found"}, status=status.HTTP_400_BAD_REQUEST)


class FullInfoForAdress(APIView):
    def get(self, request):
        adress = Adress.objects.get(pk=request.query_params.get("adress_id"))
        image_shop = ImageShop.objects.filter(shop=adress)
        data = {
            "id": adress.pk, 
            "adress": adress.adress, 
            "market": {
                "id": adress.shop.pk,
                "name": adress.shop.name,
                "short_description": adress.shop.short_description,
                "description": adress.shop.description,
                "link": adress.shop.link,
            }, 
            "lat": adress.long, 
            "long": adress.lat,
            "is_around_clock": adress.is_around_clock,

            "time": [
                [adress.monday_with, adress.monday_until],
                [adress.tuesday_with, adress.tuesday_until],
                [adress.wednesday_with, adress.wednesday_until],
                [adress.thursday_with, adress.thursday_until],
                [adress.friday_with, adress.friday_until],
                [adress.saturday_with, adress.saturday_until],
                [adress.sunday_with, adress.sunday_until],
            ],
            "phone": adress.phone,
            "timeaone": f"{adress.timezone}",
            "image": [f"/media/{i.image}" for i in image_shop],
        }
        return Response({"status": True, "data": data})