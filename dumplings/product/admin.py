from django import forms
from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.db import models
from product.models import (
    Category,
    Supplements,
    Composition,
    Products,
    Combo,
    DayWeek,
    ProductDay,
    Dimensions,
    NumberWeek,
    ProductWeek,
)





class BaseSupplementsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BaseSupplementsForm, self).__init__(*args, **kwargs)
        # Отфильтровать только продукты с is_supplement=True
        self.fields['base_supplements'].queryset = Products.objects.filter(is_supplement=True)

class ProductsAdmin(admin.ModelAdmin):
    form = BaseSupplementsForm
    list_display = ('title', 'category', 'price', 'weight')  # Перечислите поля, которые вы хотите отображать в списке товаров
    list_filter = ('category',)  # Добавьте фильтр по категории
    search_fields = ('title',)  # Добавьте поле для поиска по названию товара
    ordering = ('category', 'title')  # Установите порядок сортировки
    

admin.site.register(Products, ProductsAdmin)


admin.site.register(Category)
admin.site.register(Dimensions)
admin.site.register(Supplements)
admin.site.register(Composition)
# admin.site.register(Products)
admin.site.register(Combo)
admin.site.register(DayWeek)
admin.site.register(ProductDay)
admin.site.register(NumberWeek)
admin.site.register(ProductWeek)