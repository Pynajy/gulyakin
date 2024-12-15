from django.contrib import admin
from cart.models import (
    ProductsInCart,
    CartUser,
    SupplementsInCart,
    ComboInCart,
)
# Register your models here.

admin.site.register(ProductsInCart)
admin.site.register(CartUser)
admin.site.register(SupplementsInCart)
admin.site.register(ComboInCart)