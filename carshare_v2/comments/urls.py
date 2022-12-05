from django.urls import path

from carshare_v2.comments.views import create_new_comment, delete_comment

urlpatterns = (
    path('send/<int:commenter_id>/<int:commented_id>/', create_new_comment, name='send comment'),
    path('delete/<int:commenter_id>/<int:commented_id>/', delete_comment, name='delete comment'),
)