from django.urls import path

from carshare_v2.authorization.views import SignUpView, SignInView, SignOutView

urlpatterns = (
    path('register/', SignUpView.as_view(), name='sign up'),
    path('login/', SignInView.as_view(), name='sign in'),
    path('logout/', SignOutView.as_view(), name='sign out'),
)
