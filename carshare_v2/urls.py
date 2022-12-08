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

#total days - 14 days
#TODO: fix homepage - est 1 day
#TODO: implement tranports filter/search(with REST or not?) - est 2 days
#TODO: implement chat between users / chatroom for every transport - est 2 days
#TODO: fix UI and UX - est 3-4 days
#TODO: fix everything to fit requirements and manual test- est 2 days
#TODO: write tests and error handling and mock presentation- est 2 days
#TODO: deployment - est 1 day
