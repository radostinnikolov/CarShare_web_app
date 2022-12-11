
from rest_framework import generics
from carshare_v2.rest_api.serializers import TransportSerializer
from carshare_v2.transports.models import Transport


class TransportsAllAPI(generics.ListAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def get_queryset(self):
        from_id = self.request.query_params.get('from')
        to_id = self.request.query_params.get('to')
        date = self.request.query_params.get('date')
        time = self.request.query_params.get('time')
        status = self.request.query_params.get('status')
        queryset = self.queryset

        if from_id:
            queryset = queryset.filter(from_city_id=from_id)

        if to_id:
            queryset = queryset.filter(to_city_id=to_id)

        if date:
            queryset = queryset.filter(date__gt=date)

        if time:
            queryset = queryset.filter(time__gte=time)

        if status:
            queryset = queryset.filter(status=status)

        return queryset.all()
