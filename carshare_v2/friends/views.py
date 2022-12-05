from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from carshare_v2.friends.forms import BaseFriendRequestForm, BaseFriendForm
from carshare_v2.friends.models import FriendRequest, Friend


class FriendRequestSend(CreateView):
    model = FriendRequest
    form_class = BaseFriendRequestForm
    template_name = 'base/empty.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.requester_id = self.kwargs['requester_id']
            instance.receiver_id = self.kwargs['receiver_id']
            instance.save()
            return redirect(reverse_lazy('profile details', kwargs={
                'pk': self.kwargs['receiver_id']
            }))


class FriendRequestDelete(DeleteView):
    model = FriendRequest
    form_class = BaseFriendRequestForm

    def get_success_url(self):
        return reverse_lazy('index')


    def get_object(self, queryset=None):
        queryset = FriendRequest.objects.filter(requester_id=self.kwargs['requester_id'],
                                                receiver_id=self.kwargs['receiver_id'])
        obj = queryset.get()
        return obj


class FriendRequestAccept(CreateView):
    model = Friend
    form_class = BaseFriendForm
    template_name = 'base/empty.html'

    def remove_the_request(self, requester, receiver):
        obj = FriendRequest.objects.filter(requester_id=requester, receiver_id=receiver).get()
        return obj.delete()

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.requester_id = self.kwargs['requester_id']
            instance.receiver_id = self.kwargs['receiver_id']
            instance.save()
            self.remove_the_request(self.kwargs['requester_id'], self.kwargs['receiver_id'])
            return redirect(reverse_lazy('index'))
