
from rest_framework import generics
from carshare_v2.rest_api.serializers import TransportSerializer
from carshare_v2.transports.models import Transport


class TransportsAllAPI(generics.ListAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
