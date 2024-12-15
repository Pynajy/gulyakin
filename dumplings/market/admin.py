from django.contrib import admin
from market.models import (
    Adress,
    Siti,
    Shop,
    ImageShop,
    TimeZone,
)

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

admin.site.register(Adress)
admin.site.register(Siti)
admin.site.register(Shop)
admin.site.register(ImageShop)
admin.site.register(TimeZone)
