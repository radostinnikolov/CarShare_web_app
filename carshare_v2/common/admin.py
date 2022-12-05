from django.contrib import admin

from carshare_v2.common.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass
