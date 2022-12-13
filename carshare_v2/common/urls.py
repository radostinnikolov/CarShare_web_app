from django.urls import path
from django.views.decorators.cache import cache_page

from carshare_v2.common.views import IndexView, IndexViewNoLogin

urlpatterns = (
    path('home/', cache_page(60 * 15)(IndexView.as_view()), name='index'),
    path('', IndexViewNoLogin.as_view(), name='index no login'),
)