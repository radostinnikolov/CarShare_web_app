from django.urls import path

from carshare_v2.common.views import IndexView, IndexViewNoLogin

urlpatterns = (
    path('home/', IndexView.as_view(), name='index'),
    path('', IndexViewNoLogin.as_view(), name='index no login'),
)