from django.contrib import admin

from carshare_v2.transports.models import Transport


@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_city', 'to_city', 'driver', 'date', 'time', 'status')
    list_filter = ('id', 'from_city', 'to_city', 'driver', 'date', 'time', 'status')
    search_fields = ('id', 'from_city', 'to_city', 'driver', 'date', 'time', 'status')
    sortable_by = ('id', 'from_city', 'to_city', 'driver', 'date', 'time', 'status')
    ordering = ('date',)
