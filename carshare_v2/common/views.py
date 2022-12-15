from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from django.views import generic

from carshare_v2.common.mixins import UserUtilsMixin
from carshare_v2.friends.models import FriendRequest
from carshare_v2.transports.models import Transport

UserModel = get_user_model()


class IndexView(UserUtilsMixin, LoginRequiredMixin, generic.TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['friend_users'] = UserModel.objects.filter(id__in=self.get_friends_ids(context['user'].pk)).all()
        context['friends_transports'] = Transport.objects.filter(
            driver_id__in=self.get_friends_ids(context['user'].pk)).all().order_by('-date')
        context['my_transports'] = self.get_current_user_transports(context['user'].pk)
        context['friend_requests'] = FriendRequest.objects.filter(
            requester_id__in=self.get_requesters_ids(context['user'].pk), receiver_id=context['user'].pk)
        return context


class IndexViewNoLogin(generic.TemplateView):
    template_name = 'common/new-index.html'

    def get(self, request, *args, **kwargs):
        context = super().get(request, *args, **kwargs)
        if request.user.is_authenticated:
            return redirect('index')
        return context
