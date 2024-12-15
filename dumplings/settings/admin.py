from django.contrib import admin

from settings.models import (
    OrderSettings,
    ErrorClient,
    TelegaramBotForAdressMarket,
    AllProductsSettings,
    GlobalSettings,
)

admin.site.site_header = "Гулякин"
admin.site.site_title = "Панель администрирования"
admin.site.index_title = "Администрирование Гулякин"

admin.site.register(OrderSettings)
admin.site.register(ErrorClient)
admin.site.register(TelegaramBotForAdressMarket)
admin.site.register(AllProductsSettings)
admin.site.register(GlobalSettings)