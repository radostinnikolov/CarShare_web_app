from django.contrib import admin

from carshare_v2.ratings.models import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_profile', 'to_profile')
    list_filter = ('id', 'from_profile', 'to_profile')
    search_fields = ('id', 'from_profile', 'to_profile')
    sortable_by = ('id', 'from_profile', 'to_profile')
    ordering = ('id',)
