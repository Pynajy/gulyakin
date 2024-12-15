from django.db import models
import uuid
from datetime import datetime

from product.models import (
    Products,
    Combo,
)


def shop_image_directory_path(instance: "ImageShop", filename: str) -> str:
    return "shop/image_{pk}.jpg".format(
        pk=uuid.uuid4(),
    )


class Siti(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название города")
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        verbose_name_plural = 'Города'


class Shop(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    short_description = models.CharField(max_length=500, blank=True, verbose_name="Короткое описание")
    description = models.TextField(blank=True, verbose_name="Полное описание")
    link = models.IntegerField(default=1, verbose_name="Внутренний номер")
    products = models.ManyToManyField(Products, blank=True, verbose_name="Продукты")
    combo = models.ManyToManyField(Combo, blank=True, verbose_name="Комбо")
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        verbose_name_plural = 'Магазины'


class TimeZone(models.Model):
    title = models.CharField(max_length=500, verbose_name="Часовая зона(+2)")

    def __str__(self) -> str:
        return f'{self.title}'
    
    class Meta:
        verbose_name_plural = 'Часовые пояса'


class Adress(models.Model):
    adress = models.CharField(max_length=500, verbose_name="Адрес")
    siti = models.ForeignKey(Siti, on_delete=models.CASCADE, verbose_name="Город")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name="Магазин")
    phone = models.CharField(max_length=15, default=79991112233, verbose_name="Телефон для связи")
    long = models.FloatField(default=0.0, verbose_name="Долгота")
    lat = models.FloatField(default=0.0, verbose_name="Широта")
    timezone = models.ForeignKey(TimeZone, on_delete=models.CASCADE, default=2, verbose_name="Часовая зона")
    is_around_clock = models.BooleanField(default=False, verbose_name="Круглосуточно?")

    monday_with = models.TimeField(default=datetime.now(), verbose_name="Понедельник с")
    monday_until = models.TimeField(default=datetime.now(), verbose_name="Понедельник до")

    tuesday_with = models.TimeField(default=datetime.now(), verbose_name="Вторник с")
    tuesday_until = models.TimeField(default=datetime.now(), verbose_name="Вторник до")

    wednesday_with = models.TimeField(default=datetime.now(), verbose_name="Среда с")
    wednesday_until = models.TimeField(default=datetime.now(), verbose_name="Среда до")

    thursday_with = models.TimeField(default=datetime.now(), verbose_name="Четвер с")
    thursday_until = models.TimeField(default=datetime.now(), verbose_name="Четверг до")

    friday_with = models.TimeField(default=datetime.now(), verbose_name="Пятница с")
    friday_until = models.TimeField(default=datetime.now(), verbose_name="Пятница до")

    saturday_with = models.TimeField(default=datetime.now(), verbose_name="Суббота с")
    saturday_until = models.TimeField(default=datetime.now(), verbose_name="Суббота до")
    
    sunday_with = models.TimeField(default=datetime.now(), verbose_name="Воскресенье с")
    sunday_until = models.TimeField(default=datetime.now(), verbose_name="Воскресенье до")

    def __str__(self) -> str:
        return f'{self.adress}'
    
    class Meta:
        verbose_name_plural = 'Адреса магазинов'
    

class ImageShop(models.Model):
    shop = models.ForeignKey(Adress, on_delete=models.CASCADE, verbose_name="Магазин")
    image = models.ImageField(upload_to=shop_image_directory_path, verbose_name="Изображение")

    def __str__(self) -> str:
        return f'{self.shop}'
    
    class Meta:
        verbose_name_plural = 'Фотографии магазинов'
    