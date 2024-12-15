from django.db import models
import uuid


def products_image_directory_path(instance: "Products", filename: str) -> str:
    return "products/image_{pk}.jpg".format(
        pk=uuid.uuid4(),
    )


def category_image_directory_path(instance: "Category", filename: str) -> str:
    return "category/image_{pk}.jpg".format(
        pk=uuid.uuid4(),
    )


def supplements_image_directory_path(instance: "Supplements", filename: str) -> str:
    return "supplements/image_{pk}.jpg".format(
        pk=uuid.uuid4(),
    )

def combo_image_directory_path(instance: "Combo", filename: str) -> str:
    return "combo/image_{pk}.jpg".format(
        pk=uuid.uuid4(),
    )


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    image = models.ImageField(upload_to=category_image_directory_path, default="None", blank=True, verbose_name="Изображение")
    
    def __str__(self) -> str:
        return f'{self.title}'
    
    class Meta:
        verbose_name_plural = 'Категории'


class Supplements(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    short_description = models.CharField(max_length=500, verbose_name="Короткое описание")
    image = models.ImageField(upload_to=supplements_image_directory_path, blank=True, verbose_name="Изображение")
    price = models.FloatField(verbose_name="Цена")
    
    def __str__(self) -> str:
        return f'{self.title}'
    
    class Meta:
        verbose_name_plural = 'Добавки'


class Composition(models.Model):
    text = models.TextField(verbose_name="Состав")

    class Meta:
        verbose_name_plural = 'Состав'


class Dimensions(models.Model):
    title = models.CharField(max_length=10, verbose_name="Название")

    def __str__(self) -> str:
        return f'{self.title}'
    
    class Meta:
        verbose_name_plural = 'Единицы измерения'


class Products(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    short_description = models.CharField(max_length=500, blank=True, verbose_name="Короткое описание")
    description = models.TextField(blank=True, verbose_name="Полное описание")
    price = models.FloatField(verbose_name="Цена")
    old_price = models.FloatField(verbose_name="Старая цена", default=0.0)
    discount = models.IntegerField(default=0, verbose_name="Скидка в %")
    weight = models.IntegerField(default=0, verbose_name="Вес")
    dimensions = models.ForeignKey(Dimensions, on_delete=models.CASCADE, default=1, verbose_name="Единица измерения")
    image = models.ImageField(upload_to=products_image_directory_path, default="null.png", verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    supplements = models.ManyToManyField(Supplements, blank=True, verbose_name="Добавки")
    is_supplement = models.BooleanField(default=False, verbose_name="Является добавкой?")
    is_multiple_supplements = models.BooleanField(default=False, verbose_name="Доступна одна добавка?")
    base_supplements = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='supplemented_by', verbose_name="Продукты как добавки")
    composition = models.ForeignKey(Composition, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Состав")
    
    def __str__(self) -> str:
        return f'{self.category} | {self.title}'
    
    class Meta:
        verbose_name_plural = 'Товары'


class Combo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    products = models.ManyToManyField(Products, verbose_name="Товары")
    image = models.ImageField(upload_to=combo_image_directory_path, blank=True, verbose_name="Изображение")
    old_price = models.FloatField(verbose_name="Старая цена")
    new_price = models.FloatField(verbose_name="Новая цена")
    weight = models.IntegerField(default=0, verbose_name="Вес")
    drinks = models.ManyToManyField(Products, blank=True, related_name="drinks", verbose_name="Товар для выбора")

    def __str__(self) -> str:
        return f'{self.title}'
    
    class Meta:
        verbose_name_plural = 'Комбо'


class DayWeek(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    number_day = models.IntegerField(default=0, verbose_name="Номер дня")

    def __str__(self) -> str:
        return f'{self.title}'
    
    class Meta:
        verbose_name_plural = 'Дни недели'

from market.models import (
    Shop,
)

class ProductDay(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="Товар")
    market = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name="Магазин")
    day_week = models.ForeignKey(DayWeek, on_delete=models.CASCADE, verbose_name="День недели")

    def __str__(self) -> str:
        return f'{self.day_week}'
    
    class Meta:
        verbose_name_plural = 'Товар дня'


class NumberWeek(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    number_week = models.IntegerField(default=0, verbose_name="Номер недели")

    def __str__(self) -> str:
        return f'{self.title}'
    
    class Meta:
        verbose_name_plural = 'Недели'


class ProductWeek(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="Товар")
    market = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name="Магазин")
    day_week = models.ForeignKey(NumberWeek, on_delete=models.CASCADE, verbose_name="Неделя")

    def __str__(self) -> str:
        return f'{self.day_week}'
    
    class Meta:
        verbose_name_plural = 'Товар недели'