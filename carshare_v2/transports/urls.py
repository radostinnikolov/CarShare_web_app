from django.urls import path

from carshare_v2.transports.views import TransportsAllListView, TransportsCreateView, TransportsDetailView, \
    TransportsEditView, TransportsDeleteView, \
    send_transport_request, remove_passenger_from_transport, accept_passenger_request, reject_passenger_request, create_chatroom

urlpatterns = (
    path('all/', TransportsAllListView.as_view(), name='transports all'),
    path('create/', TransportsCreateView.as_view(), name='transports create'),
    path('details/<int:pk>/', TransportsDetailView.as_view(), name='transports details'),
    path('edit/<int:pk>/', TransportsEditView.as_view(), name='transports edit'),
    path('delete/<int:pk>/', TransportsDeleteView.as_view(), name='transports delete'),
    path('send_transport_request/<int:transport_id>/<int:user_id>/', send_transport_request,
         name='send transport request'),
    path('remove_user_from_transport/<int:transport_id>/<int:user_id>/', remove_passenger_from_transport,
         name='remove passenger'),
    path('accept_transport_request/<int:transport_id>/<int:user_id>/', accept_passenger_request,
         name='accept passenger'),
    path('reject_transport_request/<int:transport_id>/<int:user_id>/', reject_passenger_request,
         name='reject passenger'),
    path('create_chatroom/<int:transport_id>/', create_chatroom,
         name='chatroom create'),
)
