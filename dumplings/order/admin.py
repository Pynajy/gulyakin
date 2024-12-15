from django.contrib import admin
from order.models import (
    UserOrderHystory,
    DeliveryType,
    PymentType,
)

admin.site.register(UserOrderHystory)
admin.site.register(DeliveryType)
admin.site.register(PymentType)