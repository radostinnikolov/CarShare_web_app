from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from django.views import generic

from carshare_v2.friends.models import Friend, FriendRequest
from carshare_v2.transports.models import Transport

UserModel = get_user_model()


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'common/index.html'

    @staticmethod
    def get_friends_ids(pk):
        ids = [x.requester_id for x in Friend.objects.filter(receiver_id=pk)]
        ids.extend([x.receiver_id for x in Friend.objects.filter(requester_id=pk)])
        return ids

    @staticmethod
    def get_requesters_ids(pk):
        return [x.requester_id for x in FriendRequest.objects.filter(receiver_id=pk)]

    @staticmethod
    def get_current_user_transports(pk):
        current_tranports = [x for x in Transport.objects.filter(driver_id=pk).all().order_by('-date')]
        current_tranports.extend([x for x in Transport.objects.filter(passengers=pk).all().order_by('-date')])
        return current_tranports


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['friend_users'] = UserModel.objects.filter(id__in=IndexView.get_friends_ids(context['user'].pk)).all()
        context['friends_transports'] = Transport.objects.filter(driver_id__in=IndexView.get_friends_ids(context['user'].pk)).all().order_by('-date')
        context['my_transports'] = IndexView.get_current_user_transports(context['user'].pk)
        context['friend_requests'] = FriendRequest.objects.filter(requester_id__in=IndexView.get_requesters_ids(context['user'].pk), receiver_id=context['user'].pk)
        return context


class IndexViewNoLogin(generic.TemplateView):
    template_name = 'common/new-index.html'

    def get(self, request, *args, **kwargs):
        context = super().get(request, *args, **kwargs)
        if request.user.is_authenticated:
            return redirect('index')
        return context
