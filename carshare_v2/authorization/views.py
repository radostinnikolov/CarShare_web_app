from django.contrib.auth import views as auth_views, login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views import generic

from carshare_v2.authorization.forms import SignUpForm


UserModel = get_user_model()


class SignUpView(generic.CreateView):
    template_name = 'authorization/sign-up.html'
    form_class = SignUpForm

    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class SignInView(auth_views.LoginView):
    template_name = 'authorization/sign-in.html'


class SignOutView(auth_views.LogoutView):
    template_name = 'authorization/sign-out.html'