from django.urls import path
from django.views.decorators.cache import cache_page

from carshare_v2.rest_api.views import TransportsAllAPI

urlpatterns = (
    path('transports/', TransportsAllAPI.as_view(), name='all transports api'),
)