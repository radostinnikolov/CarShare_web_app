from django.urls import path

from carshare_v2.ratings.views import rate_user

urlpatterns = (
    path('give_rating/<int:giver_id>/<int:receiver_id>/', rate_user, name='give rating'),
)