from django.db import models

from market.models import (
    Adress,
    Siti,
)


class ListBooing(models.Model):
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE, verbose_name="Адрес")
    siti = models.ForeignKey(Siti, on_delete=models.CASCADE, default=2, verbose_name="Город")

    def __str__(self) -> str:
        return f'{self.adress}'
    
    class Meta:
        verbose_name_plural = 'Адреса для бронирования'


class BookingModel(models.Model):
    adress = models.ForeignKey(ListBooing, on_delete=models.CASCADE, default=1, verbose_name="Адрес")
    time = models.CharField(max_length=10, verbose_name="Время")
    date = models.CharField(max_length=20, default=1, verbose_name="Дата")
    count_guest = models.IntegerField(verbose_name="Количество гостей")
    name = models.CharField(max_length=50, verbose_name="Имя")
    phone = models.CharField(max_length=15, verbose_name="Телефон")

    def __str__(self) -> str:
        return f'{self.phone}'
    
    class Meta:
        verbose_name_plural = 'Заявки на бронирование'