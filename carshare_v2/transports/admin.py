from django.contrib import admin

from carshare_v2.transports.models import Transport


@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    pass
