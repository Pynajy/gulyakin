from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

from datetime import datetime
import re

from market.models import (
    Shop,
)

from product.models import (
    Products,
    Combo,
    ProductDay,
    DayWeek,
    Supplements,
    ProductWeek,
    NumberWeek,
)

from settings.models import (
    AllProductsSettings,
)

from product.tools.product_week import (
    week_number_in_month
)

class GetSouse(APIView):
    def get(self, request):
        products = Products.objects.filter(category=10)
        aps = AllProductsSettings.objects.last()
        product = [{
            "id": i.pk,
            "title": i.title,
            "short_description": i.short_description,
            "description": i.description,
            "price": i.price,
            "is_discount": (True if (((i.price / 100) * aps.total_discount) + ((i.price / 100) * i.discount)) != 0 else False),
            "price_discount": i.price - ((i.price / 100) * aps.total_discount) - ((i.price / 100) * i.discount),
            "old_price": i.old_price,
            "image": f"/media/{i.image}",
            "category": i.category.pk,
            "weight": i.weight,
            "is_multiple_supplements": i.is_multiple_supplements,
            "supplements": [{
                "id": j[0],
                "title": j[1],
                "short_description": j[2],
                "image": j[3],
                "price": (j[4] if not i.is_multiple_supplements else 0)
            } for j in i.supplements.values_list()],
            "composition": (i.composition.text if i.composition else ""),
        } for i in products]

        return Response({"status": True, "souse": product})


class GetProductInMarket(APIView):
    def get(self, request):
        aps = AllProductsSettings.objects.last()
        market_id = request.query_params.get("market_id")
        # Товар дня
        date_pattern = re.compile(r'^\d{2}-\d{2}-\d{4}$')
        date = request.query_params.get("date")
        if date_pattern.match(date):
            date_object = datetime.strptime(date, "%d-%m-%Y")

            # # Получить день недели в виде числа (0 - понедельник, 6 - воскресенье)
            day_of_week = date_object.weekday()

            day_week = DayWeek.objects.filter(number_day=day_of_week).first()

            product_day = ProductDay.objects.filter(day_week=day_week, market=market_id).first()

            if product_day:
                product_day_id = product_day.product.pk
            else:
                product_day_id = 0

        # Товар недели
        week_num = NumberWeek.objects.get(number_week=week_number_in_month(date))
        product_week = ProductWeek.objects.filter(day_week=week_num, market=market_id).first()
        if product_week:
            product_week_id = product_week.product.pk
        else:
            product_week_id = 0
        print(product_week_id)


        market = Shop.objects.filter(pk=market_id).first()
        if not market:
            return Response({"status": False, "error": "market_not_found"}, status=status.HTTP_404_NOT_FOUND)
        products = Products.objects.filter(pk__in=[int(i[0]) for i in market.products.values_list()])
        product = [{
            "id": i.pk,
            "is_product_day": (True if i.pk == product_day_id else False),
            "is_product_week": (True if i.pk == product_week_id else False),
            "title": i.title,
            "short_description": i.short_description,
            "description": i.description,
            "price": i.price,
            "is_discount": (True if (((i.price / 100) * aps.total_discount) + ((i.price / 100) * i.discount)) != 0 else False),
            "price_discount": i.price - ((i.price / 100) * aps.total_discount) - ((i.price / 100) * i.discount),
            "old_price": i.old_price,
            "image": f"/media/{i.image}",
            "category": i.category.pk,
            "weight": i.weight,
            "dimensions": i.dimensions.title,
            "is_multiple_supplements": i.is_multiple_supplements,
            "supplements": [{
                "id": j[0],
                "title": j[1],
                "short_description": j[2],
                "image": j[3],
                "price": (j[4] if not i.is_multiple_supplements else 0)
            } for j in i.supplements.values_list()],
            "composition": (i.composition.text if i.composition else ""),
        } for i in products]
        base_supplements = []
        for i in products:
            if i.is_supplement:
                base_supplements.append({
                    "id": i.pk,
                    "title": i.title,
                    "price": i.price,
                    "image": f"/media/{i.image}",
                    "category": i.category.pk,
                })

        return Response({"status": True, 
                         "products": product, 
                         "base_supplements": base_supplements, 
                         })
    

class GetCategoryInMarket(APIView):
    def get(self, request):
        market_id = request.query_params.get("market_id")
        market = Shop.objects.filter(pk=market_id).first()
        if not market:
            return Response({"status": False, "error": "market_id_not_found"}, status=status.HTTP_201_CREATED)
        products = Products.objects.filter(pk__in=[int(i[0]) for i in market.products.values_list()])
        category = [{
            "id": i.category.pk,
            "title": i.category.title,
            "image": f"/media/{i.category.image}",
        } for i in products]

        unique_ids = set()
        unique_data = []
        for item in category:
            if item["id"] not in unique_ids:
                unique_data.append(item)
                unique_ids.add(item["id"])

        return Response({"status": True, "category": unique_data})


class GetComboForMarket(APIView):
    def get(self, request):
        shop_id = request.query_params.get("market_id")
        shop = Shop.objects.get(pk=shop_id)
        list_combo = shop.combo.values_list("pk")
        combos = []
        for i in list_combo:
            combo = Combo.objects.get(pk=i[0])
            data_combo = {
                "id": combo.pk,
                "title": combo.title,
                "image": f"/media/{combo.image}",
                "weight": combo.weight,
                "old_price": combo.old_price,
                "price": combo.new_price,
                "products": [],
                "drinks": []  # Добавлено поле "drinks"
            }
            for j in combo.products.values_list("pk"):
                product = Products.objects.get(pk=j[0])
                data_products = {
                    "id": product.pk,
                    "title": product.title
                }
                data_combo["products"].append(data_products)
            for k in combo.drinks.values_list("pk"):  # Получение товаров из "drinks"
                drink = Products.objects.get(pk=k[0])
                data_drinks = {
                    "id": drink.pk,
                    "title": drink.title,
                    "image": f"/media/{drink.image}",
                }
                data_combo["drinks"].append(data_drinks)
            combos.append(data_combo)
        return Response({"status": True, "combos": combos})


class GetProductDayForMarket(APIView):
    def get(self, request):
        date_pattern = re.compile(r'^\d{2}-\d{2}-\d{4}$')
        date = request.query_params.get("date")
        if date_pattern.match(date):
            aps = AllProductsSettings.objects.last()
            market_id = request.data["market_id"]
            date_object = datetime.strptime(date, "%d-%m-%Y")

            # # Получить день недели в виде числа (0 - понедельник, 6 - воскресенье)
            day_of_week = date_object.weekday()
            print(day_of_week)

            day_week = DayWeek.objects.filter(number_day=day_of_week).first()
            print(day_week)

            product_day = ProductDay.objects.filter(day_week=day_week, market=market_id).first()

            if product_day:
                data_product = {
                    "id": product_day.product.pk,
                    "title": product_day.product.title,
                    "short_description": product_day.product.short_description,
                    "description": product_day.product.description,
                    "price": product_day.product.price,
                    "is_discount": (True if (((product_day.product.price / 100) * aps.total_discount) + ((product_day.product.price / 100) * product_day.product.discount)) != 0 else False),
                    "price_discount": product_day.product.price - ((product_day.product.price / 100) * aps.total_discount) - ((product_day.product.price / 100) * product_day.product.discount),
                    "old_price": product_day.product.old_price,
                    "weight": product_day.product.weight,
                    "image": f"/media/{product_day.product.image}",
                    "category": f"{product_day.product.category}",
                    "composition": f"{product_day.product.composition.text}",
                }

                return Response({"status": True, "product": data_product})
            else:
                return Response({"status": False, "error": "product_not_found"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return  Response({"status": False, "error": "invalid_date_format"}, status=status.HTTP_400_BAD_REQUEST)


class GetSupplementsForId(APIView):
    def get(self, request):
        id_list_supplements = request.query_params.get("list_supplements")
        supplements = Supplements.objects.filter(pk__in=id_list_supplements)
        data_supplements = []
        for i in supplements:
            data_supplements.append({
                "id": i.pk,
                "title": i.title,
                "short_description": i.short_description,
                "image": f"/media/{i.image}",
                "price": i.price
            })
        return Response({"status": True, "supplements": data_supplements})