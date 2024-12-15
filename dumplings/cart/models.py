from django.db import models
from django.contrib.auth.models import User

from product.models import (
    Products,
    Supplements,
    Combo,
)

class SupplementsInCart(models.Model):
    supplements = models.ForeignKey(Supplements, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Добавки")
    count = models.IntegerField(verbose_name="Количество")

    def __str__(self) -> str:
        return f'{self.supplements}'
    
    class Meta:
        verbose_name_plural = 'Добавки в корзине'


class ComboInCart(models.Model):
    combo = models.ForeignKey(Combo, on_delete=models.CASCADE, verbose_name="Комбо")
    selected_product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="Выбранный продукт")
    
    def __str__(self) -> str:
        return f'{self.combo}'
    
    class Meta:
        verbose_name_plural = 'Комбо в корзине'


class ProductsInCart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Продукт")
    supplements = models.ManyToManyField(SupplementsInCart, blank=True, verbose_name="Добавки")
    is_combo = models.BooleanField(default=False, verbose_name="Является 'комбо'?")
    combo = models.ForeignKey(ComboInCart, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Комбо в корзине")
    count = models.IntegerField(verbose_name="Количество")

    def __str__(self) -> str:
        return f'{self.product if self.product else self.combo}'
    
    class Meta:
        verbose_name_plural = 'Продукты в корзине'


class CartUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    products = models.ManyToManyField(ProductsInCart, verbose_name="Продукты")

    def __str__(self) -> str:
        return f'{self.user}'
    
    class Meta:
        verbose_name_plural = 'Корзины'