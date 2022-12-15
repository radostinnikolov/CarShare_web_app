from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('carshare_v2.authorization.urls')),
    path('', include('carshare_v2.common.urls')),
    path('profile/', include('carshare_v2.accounts.urls')),
    path('friend/', include('carshare_v2.friends.urls')),
    path('transports/', include('carshare_v2.transports.urls')),
    path('comment/', include('carshare_v2.comments.urls')),
    path('rate/', include('carshare_v2.ratings.urls')),
    path('api/', include('carshare_v2.rest_api.urls')),
    path('chat/', include('carshare_v2.chat.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


