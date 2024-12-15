from django.urls import path, include

from settings.views import (
    GetErrorInClient,
    TestDistribution,
    GetOrderSettings,
    GetGlobalSettings,
)

urlpatterns = [
    path('error', GetErrorInClient.as_view(), name='GetErrorInClient'),
    path('distribution', TestDistribution.as_view(), name='TestDistribution'),
    path('order-settings', GetOrderSettings.as_view(), name='GetOrderSettings'),
    path('global', GetGlobalSettings.as_view(), name='GetGlobalSettings'),
]