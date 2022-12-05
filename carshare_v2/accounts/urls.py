from django.urls import path, include

from carshare_v2.accounts.views import ProfileDetailsView, ProfileEditView, ProfileDeleteView

urlpatterns = (
    path('details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('edit/<int:pk>/', ProfileEditView.as_view(), name='profile edit'),
    path('delete/<int:pk>/', ProfileDeleteView.as_view(), name='profile delete')
)
