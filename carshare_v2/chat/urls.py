from django.urls import path

from carshare_v2.chat.views import IndexChatTemplateView, room

urlpatterns = (
    path('', IndexChatTemplateView.as_view(), name='index-chat'),
    path("<str:room_name>/", room, name="room"),
)