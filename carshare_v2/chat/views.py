from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from carshare_v2.transports.models import Transport


from django.contrib.sessions.models import Session
from django.utils import timezone

UserModel = get_user_model()

def get_all_logged_in_users():
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    uid_list = []

    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))

    return UserModel.objects.filter(id__in=uid_list)


class IndexChatTemplateView(TemplateView):
    template_name = "chat/index-chat.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


def room(request, room_name):
    current_transport = Transport.objects.filter(chatroom_name=room_name).get()
    current_users = get_all_logged_in_users()


    if request.method == 'GET':
        if request.user not in current_transport.passengers.all() and request.user != current_transport.driver:
            return redirect('index-chat')

        else:
            current_online_in_chatroom = [x for x in current_users if x in current_transport.passengers.all() or x == current_transport.driver]

            context = {
                "room_name": room_name,
                'user': request.user,
                'online': current_online_in_chatroom
            }
            return render(request, "chat/room.html", context)

