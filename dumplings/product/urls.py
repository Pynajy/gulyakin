from django.urls import path, include

from product.views import (
    GetProductInMarket,
    GetCategoryInMarket,
    GetComboForMarket,
    GetProductDayForMarket,
    GetSupplementsForId,
    GetSouse,
)

urlpatterns = [
    path('in-market', GetProductInMarket.as_view(), name='GetProductInMarket'),
    path('category', GetCategoryInMarket.as_view(), name='GetCategoryInMarket'),
    path('combo', GetComboForMarket.as_view(), name='GetComboForMarket'),
    path('day', GetProductDayForMarket.as_view(), name='GetProductDayForMarket'),
    path('supplements', GetSupplementsForId.as_view(), name='GetSupplementsForId'),
    path('souse', GetSouse.as_view(), name='GetSouse'),
]