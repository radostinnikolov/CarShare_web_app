from django.urls import path

from carshare_v2.friends.views import FriendRequestSend, FriendRequestDelete, FriendRequestAccept

urlpatterns = (
    path('send_request/<int:requester_id>/<int:receiver_id>', FriendRequestSend.as_view(), name='friend request send'),
    path('reject_request/<int:requester_id>/<int:receiver_id>', FriendRequestDelete.as_view(), name='friend request reject'),
    path('accept_request/<int:requester_id>/<int:receiver_id>', FriendRequestAccept.as_view(), name='friend request accept'),
)