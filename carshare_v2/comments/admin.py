from django.contrib import admin

from carshare_v2.comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_profile', 'to_profile', 'date_of_publication')
    list_filter = ('id', 'from_profile', 'to_profile', 'date_of_publication')
    search_fields = ('id', 'from_profile', 'to_profile', 'date_of_publication')
    sortable_by = ('id', 'from_profile', 'to_profile', 'date_of_publication')
    ordering = ('date_of_publication',)
