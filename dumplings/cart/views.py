from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from cart.models import (
    ProductsInCart,
    CartUser,
    SupplementsInCart,
    ComboInCart,
)

from product.models import (
    Products,
    Combo,
)

from settings.models import (
    AllProductsSettings,
)


class AddToCart(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        user = User.objects.get(pk=request.user.id)
        products_data = request.data["products"]

        # Создаем корзину пользователя (если не существует)
        cart_user, created = CartUser.objects.get_or_create(user=user)
        
        list_id_products_in_cart = []

        # Перебираем ваши входные данные и создаем объекты ProductsInCart
        for product_data in products_data:
            product_id = product_data["product"]
            supplements_data = product_data["supplements"]
            count = product_data["count"]

            # Получаем или создаем объект ProductsInCart
            product_in_cart, created = ProductsInCart.objects.get_or_create(
                product_id=product_id,
                count=count
            )

            list_id_products_in_cart.append(product_in_cart.pk)

            # Очищаем список supplements в product_in_cart, чтобы заменить его новыми данными
            product_in_cart.supplements.clear()

            

            # Добавляем дополнения к продукту
            for supplement_data in supplements_data:
                supplement_id = supplement_data["id"]
                supplement_count = supplement_data["count"]

                # Получаем или создаем объект SupplementsInCart
                supplement_in_cart = SupplementsInCart.objects.filter(
                    supplements_id=supplement_id,
                    count=supplement_count
                )
                if len(supplement_in_cart) < 2:
                    supplement_in_cart, created = SupplementsInCart.objects.get_or_create(
                        supplements_id=supplement_id,
                        count=supplement_count
                    )
                elif len(supplement_in_cart) > 1:
                    supplement_in_cart = SupplementsInCart.objects.filter(
                    supplements_id=supplement_id,
                    count=supplement_count
                ).first()
                else:
                    supplement_in_cart, created = SupplementsInCart.objects.create(
                        supplements_id=supplement_id,
                        count=supplement_count
                    )
                # Добавляем объект SupplementsInCart к product_in_cart
                product_in_cart.supplements.add(supplement_in_cart)

            # Добавляем объект ProductsInCart в корзину пользователя
            cart_user.products.add(product_in_cart)
        
        return Response({"status": True, "list_id": list_id_products_in_cart}, status=status.HTTP_201_CREATED)


class ListCart(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        aps = AllProductsSettings.objects.last()
        user = User.objects.get(pk=request.user.id)
        cart_user, created = CartUser.objects.get_or_create(user=user)
        if not cart_user:
            return Response({"status": False, "error": "cart_user_not_found"}, status=status.HTTP_404_NOT_FOUND)
        cart = []
        total_price = 0.0  # Общая цена корзины
        total_price_discount = 0.0
        supplement_counts = {}  # Словарь для подсчета количества каждой добавки

        for product_in_cart in cart_user.products.all():
            product = product_in_cart.product
            is_combo = product_in_cart.is_combo

            # Если продукт является комплектом, обрабатываем его по-другому
            if is_combo:
                combo = product_in_cart.combo
                combo_data = {
                    "id": combo.combo.id,
                    "title": combo.combo.title,
                    "image": f"/media/{combo.combo.image}",
                    "old_price": combo.combo.old_price,
                    "price": combo.combo.new_price,
                    "products": [{
                        "id": product.id,
                        "title": product.title
                        } for product in combo.combo.products.all()],
                    "drinks": [{
                        "id": drink.id,
                        "title": drink.title
                        } for drink in combo.combo.drinks.all()],
                    "selected_product": {
                        "id": combo.selected_product.id,
                        "title": combo.selected_product.title,
                        "image": f"/media/{combo.selected_product.image}",

                        # Добавьте остальные поля выбранного продукта, если необходимо
                    },
                }
                total_price += combo.combo.new_price * product_in_cart.count
                cart.append({"is_combo": True, "id": product_in_cart.pk, "product": combo_data, "count": product_in_cart.count})
                continue

            # Продолжаем обработку остальных продуктов
            product_price = product.price

            # Считаем общую цену с учетом дополнений
            total_price += product_price * product_in_cart.count
            total_price_discount += (product.price - ((product.price / 100) * aps.total_discount) - ((product.price / 100) * product.discount)) * product_in_cart.count

            # Создаем список дополнений для данного продукта
            supplements_list = []
            for supplement_in_cart in product_in_cart.supplements.all():
                supplement = supplement_in_cart.supplements
                supplement_price = supplement.price * supplement_in_cart.count
                total_price += (supplement_price if not product_in_cart.product.is_multiple_supplements else 0)
                supplements_list.append({
                    "id": supplement.id,
                    "supplement_in_cart_id": supplement_in_cart.id,
                    "title": supplement.title,
                    "short_description": supplement.short_description,
                    "image": f"/media/{supplement.image}",
                    "price": (supplement_price if not product_in_cart.product.is_multiple_supplements else 0)
                    # "price": supplement_price,
                })

                # Обновляем подсчет количества каждой добавки
                if supplement.id in supplement_counts:
                    supplement_counts[supplement.id] += supplement_in_cart.count
                else:
                    supplement_counts[supplement.id] = supplement_in_cart.count

            # Создаем элемент корзины
            elem = {
                "is_combo": product_in_cart.is_combo,
                "id": product_in_cart.id,
                "product": {
                    "id": product.pk,
                    "title": product.title,
                    "short_description": product.short_description,
                    "description": product.description,
                    "price": product_price,
                    "is_discount": (True if (((product.price / 100) * aps.total_discount) + ((product.price / 100) * product.discount)) != 0 else False),
                    "price_discount": product.price - ((product.price / 100) * aps.total_discount) - ((product.price / 100) * product.discount),
                    "old_price": product.old_price,
                    "weight": product.weight,
                    "dimensions": product.dimensions.title,
                    "is_multiple_supplements": product.is_multiple_supplements,
                    "image": f"/media/{product.image}",
                    "composition": (product.composition.text if product.composition else ""),
                },
                "count": product_in_cart.count,
                "supplements": supplements_list,
            }
            cart.append(elem)

        return Response({"status": True, "cart": cart, "price": total_price, "total_price_discount": total_price_discount, "supplement_counts": supplement_counts})


class EditCountCart(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        cart_id = request.data["cart_id"]
        count = request.data["count"]
        product_in_cart = ProductsInCart.objects.get(pk=cart_id)
        if product_in_cart:
            product_in_cart.count = count
            product_in_cart.save()
            return Response({"status": True, "id": product_in_cart.pk})
        else:
            return Response({"status": False, "message": "cart_id not found"}, status=status.HTTP_404_NOT_FOUND )


class UpdateSupplementsInCart(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        supplements_data = request.data.get("supplements", [])
        cart_id = request.data.get("cart_id")
        print(supplements_data)

        supplements_list = []
        pic = ProductsInCart.objects.filter(pk=cart_id).first()
        if not pic:
            return Response({"status": False, "error": f"cart_id: {suppl['cart_id']} not found"}, status=status.HTTP_400_BAD_REQUEST)
        pic.supplements.clear()

        for suppl in supplements_data:
            if suppl["added"]:
                sic = SupplementsInCart.objects.create(
                    supplements_id = suppl["supplements_id"],
                    count = 1
                )
                pic.supplements.add(sic)
                pic.save()
                supplements_list.append({
                    "id": sic.supplements.pk,
                    "title": sic.supplements.title,
                    "short_description": sic.supplements.short_description,
                    "image": f"/media/{sic.supplements.image}",
                    "price": sic.supplements.price
                })
        return Response({"status": True, "supplements_list": supplements_list}, status=status.HTTP_200_OK)


class DeleteCart(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        cart_id = request.data["cart_id"]
        product_in_cart = ProductsInCart.objects.get(pk=cart_id)
        if product_in_cart:
            product_in_cart.delete()
            return Response({"status": True})
        else:
            return Response({"status": False, "message": "cart_id not found"}, status=status.HTTP_404_NOT_FOUND)


class AddCombo(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        user = User.objects.get(pk=request.user.id)
        combos = request.data["combo"]

        list_id_products_in_cart = []
        for combo in combos:
            combo_object = Combo.objects.filter(pk=combo["id"]).first()
            cic = ComboInCart.objects.create(
                combo = combo_object,
                selected_product = Products.objects.filter(pk=combo["selected_product"]).first()
            )

            pic = ProductsInCart.objects.create(
                combo=cic,
                count = combo["count"],
                is_combo = True
            )

            cart_user, created = CartUser.objects.get_or_create(user=user)
            cart_user.products.add(pic)
            list_id_products_in_cart.append(pic.pk)
        
        return Response({"status": True, "list_id": list_id_products_in_cart}, status=status.HTTP_201_CREATED)


class DeleteCombo(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        combos = request.data["combos"]
        for combo in combos:
            pic = ProductsInCart.objects.filter(pk=combo["id"]).first()
            if pic:
                pic.delete()
            else:
                return Response({"status": False, "error": f"combo {combo['id']} in cart not found"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"status": True})


class UpdateComboInCart(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        combos = request.data["combos"]

        list_update_combo_in_cart = []
        for combo in combos:
            pic = ProductsInCart.objects.filter(pk=combo["id"]).first()
            if pic:
                if "selected_product" in combo:
                    pic.combo.selected_product = Products.objects.get(pk=combo["selected_product"])
                    pic.combo.save()
                if "count" in combo:
                    pic.count = combo["count"]
                    pic.save()
                combo_db = pic.combo
                combo_data = {
                    "id": combo_db.combo.id,
                    "title": combo_db.combo.title,
                    "image": f"/media/{combo_db.combo.image}",
                    "old_price": combo_db.combo.old_price,
                    "price": combo_db.combo.new_price,
                    "weight": combo_db.combo.weight,
                    "products": [{
                        "id": product.id,
                        "title": product.title
                        } for product in combo_db.combo.products.all()],
                    "drinks": [drink.title for drink in combo_db.combo.drinks.all()],
                    "selected_product": {
                        "id": combo_db.selected_product.id,
                        "title": combo_db.selected_product.title,
                        "image": f"/media/{combo_db.selected_product.image}",

                        # Добавьте остальные поля выбранного продукта, если необходимо
                    },
                }
                list_update_combo_in_cart.append({"is_combo": True, "id": pic.pk, "product": combo_data, "count": pic.count})
            else:
                return Response({"status": False, "error": f"combo {combo['id']} in cart not found"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"status": True, "product": list_update_combo_in_cart})


class CleatCart(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = User.objects.get(pk=request.user.id)

        cart_user, created = CartUser.objects.get_or_create(user=user)
        cart_user.products.clear()

        return Response({"status": True})
            