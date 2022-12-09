from django.contrib import admin

from carshare_v2.friends.models import FriendRequest, Friend


@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'requester', 'receiver')
    list_filter = ('id', 'requester', 'receiver')
    search_fields = ('id', 'requester', 'receiver')
    sortable_by = ('id', 'requester', 'receiver')
    ordering = ('id',)


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('id', 'requester', 'receiver')
    list_filter = ('id', 'requester', 'receiver')
    search_fields = ('id', 'requester', 'receiver')
    sortable_by = ('id', 'requester', 'receiver')
    ordering = ('id',)
