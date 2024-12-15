from django.db import models
from django.contrib.auth.models import User
from cart.models import ProductsInCart
from lk.models import Adress

from settings.models import (
    AllProductsSettings,
)

from market.models import Adress as AdressMarket

from settings.models import (
    OrderSettings,
)

from cart.models import (
    ComboInCart
)

class DeliveryType(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self) -> str:
        return f'{self.title}'
    
    class Meta:
        verbose_name_plural = 'Типы доставки'


class PymentType(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    is_payment = models.BooleanField(default=True, verbose_name="Требует оплаты?")

    def __str__(self) -> str:
        return f'{self.title}'
    
    class Meta:
        verbose_name_plural = 'Типы оплаты'


class UserOrderHystory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    products = models.ManyToManyField(ProductsInCart, blank=True, verbose_name="Продукты")
    combos = models.ManyToManyField(ComboInCart, verbose_name="Комбо")  # Добавьте поле для комбо-продуктов
    datetime = models.DateTimeField(auto_now=True, verbose_name="Дата и время")
    price = models.FloatField(null=True, blank=True, verbose_name="Цена")
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE, blank=True, verbose_name="Адрес доставки")
    delivery_type = models.ForeignKey(DeliveryType, on_delete=models.CASCADE, default=1, verbose_name="Тип доставки")
    is_call = models.BooleanField(default=True, verbose_name="Требуется звонок?")
    pyment_type = models.ForeignKey(PymentType, on_delete=models.CASCADE, default=1, verbose_name="Тип оплаты")
    change_with = models.FloatField(blank=True, default=0, verbose_name="Сдача с")
    count_tools = models.IntegerField(default=1) 
    discount = models.IntegerField(default=0)
    market_adress_id = models.ForeignKey(AdressMarket, on_delete=models.CASCADE, blank=True, verbose_name="Адрес приготовления")
    pyment_id = models.CharField(max_length=700, blank=True, default="None", verbose_name="Номер оплаты")
    time_delivery = models.CharField(max_length=50, blank=True, default="None", verbose_name="Время доставки")
    is_pyment = models.BooleanField(default=False, verbose_name="Оплачено?")
    is_activ = models.BooleanField(default=True, verbose_name="Активно?")

    @classmethod
    def create_order_from_cart_user(cls, 
                                    cart_user, 
                                    adress_id=21, 
                                    is_call=True, 
                                    delivery_type=1, 
                                    pyment_type=1, 
                                    time_delivery="40 min", 
                                    market_adress_id=12,
                                    change_with=0,
                                    count_tools=1,
                                    ):
        order_settings = OrderSettings.objects.last()
        
        print(market_adress_id)

        try:
            adress = Adress.objects.get(pk=adress_id)
        except Adress.DoesNotExist:
            raise Adress.DoesNotExist("Adress with the provided ID does not exist.")
        
        order = cls(user=cart_user.user)
        order.count_tools = count_tools
        aps = AllProductsSettings.objects.last()
        order.discount = aps.total_discount
        
        total_price = 0.0
        if len(cart_user.products.all()) < 1:
            return {"status": False, "error": "null_products_in_cart"}
        
        for product_in_cart in cart_user.products.all():
            if not product_in_cart.is_combo:
                product = product_in_cart.product
                # total_price += product.price * product_in_cart.count
                total_price += (product.price - ((product.price / 100) * aps.total_discount) - ((product.price / 100) * product.discount)) * product_in_cart.count
                for supplement_in_cart in product_in_cart.supplements.all():
                    supplement = supplement_in_cart.supplements
                    total_price += (supplement.price if not product_in_cart.product.is_multiple_supplements else 0)

        # Обработка комбо-продуктов
        for combo_in_cart in cart_user.products.all():
            if combo_in_cart.is_combo:
                combo = combo_in_cart.combo.combo
                total_price += combo.new_price

        if change_with != 0:
            order.change_with = change_with

        delivery_type_obj = DeliveryType.objects.filter(pk=delivery_type).first()
        if delivery_type_obj:
            order.delivery_type = delivery_type_obj
        else:
            return {"status": False, "error": "delivery_type_not_found"}
        
        if delivery_type == 1:
            order.price = total_price + order_settings.auto_price_delivery
        elif delivery_type == 2:
            order.price = total_price + order_settings.people_price_delivery
        else:
            order.price = total_price
        
        order.time_delivery = time_delivery
        

        pyment_type_obj = PymentType.objects.filter(pk=pyment_type).first()
        if pyment_type_obj:
            order.pyment_type = pyment_type_obj
        else:
            return {"status": False, "error": "payment_type_not_found"}
        market_adress_instance = AdressMarket.objects.get(pk=market_adress_id)
        adress_instance = Adress.objects.get(pk=adress_id)
        if delivery_type == 3:
            order.market_adress_id = market_adress_instance
            order.adress = adress_instance  # Установите адрес
        else:
            order.adress = adress_instance
            order.market_adress_id = market_adress_instance
        order.is_call = is_call

        if delivery_type == 2:
            print(total_price)
            print(order_settings.min_prise_auto)
            if total_price < order_settings.min_prise_auto:
                    return {"status": False, "error": "no_minimum_order_amount", "total_price": total_price}
        elif delivery_type == 1:
            print(total_price)
            print(order_settings.min_prise_people)
            if total_price < order_settings.min_prise_people:
                    return {"status": False, "error": "no_minimum_order_amount"}
        order.save()

        for product_in_cart in cart_user.products.all():
            order.products.add(product_in_cart)

        # Добавьте комбо-продукты в заказ
        for combo_in_cart in cart_user.products.all():
            if combo_in_cart.is_combo:
                order.combos.add(combo_in_cart.combo)

        return order

    def format_order_info(self):
        order_info = f"Заказ #{self.id}\n"
        order_info += f"Пользователь: {self.user.username}\n"
        order_info += "Товары:\n"

        for product_in_cart in self.products.all():
            if not product_in_cart.is_combo:
                order_info += f"- {product_in_cart.product.title} ({product_in_cart.count} шт.)\n"
                
                for supplement_in_cart in product_in_cart.supplements.all():
                    order_info += f"  - {supplement_in_cart.supplements.title} ({supplement_in_cart.count} шт.)\n"
        
        for product_in_cart in self.products.all():
            if product_in_cart.is_combo:
                order_info += f"- {product_in_cart.combo.combo.title} ({product_in_cart.count} шт.)\n"
                order_info += f"  - {product_in_cart.combo.selected_product.title}\n"

        order_info += f"Сумма заказа: {self.price} рублей\n"
        order_info += f"Тип доставки: {self.delivery_type.title}\n"
        order_info += f"Количество приборов: {self.count_tools}\n"
        if self.delivery_type.pk != 3:
            order_info += f"Адрес доставки: {self.adress}\n"
            order_info += f"Адрес квартира: {self.adress.apartment}\n"  
            order_info += f"Адрес подъезд: {self.adress.entrance}\n"
            order_info += f"Адрес этаж: {self.adress.floor}\n"
            order_info += f"Адрес код двери: {self.adress.door_code}\n"
        else:
            order_info += f"Адрес самовывоза: {self.market_adress_id}\n"
        order_info += f"Тип оплаты: {self.pyment_type.title}\n"
        if self.delivery_type.pk != 3:
            order_info += f"Время доставки: {self.time_delivery}\n"
        else:
            order_info += f"Время получения: {self.time_delivery}\n"
        order_info += f"Способ оплаты: {self.pyment_type}\n"
        if self.change_with != 0:
            order_info += f"Нужна сдача с {self.change_with} рублей\n"
        order_info += f"Нужен звонок оператора: {('Да' if self.is_call else 'Нет')}\n"
        if self.pyment_type.pk == 1:
            order_info += f"Статус оплаты: {'Оплачено' if self.is_pyment else 'Ожидает оплаты'}\n"

        return order_info

    def __str__(self) -> str:
        return f'{self.user}'
    
    class Meta:
        verbose_name_plural = 'Заказы'
