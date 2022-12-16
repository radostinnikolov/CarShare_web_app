from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


from carshare_v2.transports.forms import CreateTransportForm, EditTransportForm
from carshare_v2.transports.models import Transport


UserModel = get_user_model()


class TransportsAllListView(LoginRequiredMixin, ListView):
    model = Transport
    template_name = 'transports/transports-all.html'
    ordering = 'date'



class TransportsCreateView(LoginRequiredMixin, CreateView):
    model = Transport
    form_class = CreateTransportForm
    template_name = 'transports/transports-create.html'

    success_url = reverse_lazy('transports all')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.driver_id = self.request.user.pk
            instance.save()
            return redirect(self.success_url)
        return render(request, 'transports/transports-create.html', context={'form': form})


class TransportsDetailView(LoginRequiredMixin, DetailView):
    model = Transport
    template_name = 'transports/transports-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['free_seats'] = int(self.object.total_seats - self.object.passengers.count())
        return context


class TransportsEditView(LoginRequiredMixin, UpdateView):
    model = Transport
    template_name = 'transports/transports-edit.html'
    form_class = EditTransportForm

    def get_success_url(self):
        return reverse_lazy('transports details', kwargs={
            'pk': self.object.pk
        })


class TransportsDeleteView(LoginRequiredMixin, DeleteView):
    model = Transport
    template_name = 'transports/transports-delete.html'
    success_url = reverse_lazy('transports all')


@login_required
def send_transport_request(request, transport_id, user_id):
    current_transport = Transport.objects.filter(pk=transport_id).get()
    current_user = UserModel.objects.filter(pk=user_id).get()
    if request.method == 'POST':
        current_transport.requests.add(current_user)
        current_transport.save()
        return redirect(reverse_lazy('transports details', kwargs={
            'pk': transport_id
        }))

@login_required
def remove_passenger_from_transport(request, transport_id, user_id):
    current_transport = Transport.objects.filter(pk=transport_id).get()
    current_user = UserModel.objects.filter(pk=user_id).get()
    if request.method == 'POST':
        current_transport.passengers.remove(current_user)
        current_transport.save()
        return redirect(reverse_lazy('transports details', kwargs={
            'pk': transport_id
        }))

@login_required
def accept_passenger_request(request, transport_id, user_id):
    current_transport = Transport.objects.filter(pk=transport_id).get()
    current_user = UserModel.objects.filter(pk=user_id).get()
    if request.method == 'POST':
        current_transport.passengers.add(current_user)
        current_transport.requests.remove(current_user)
        current_transport.save()
        return redirect(reverse_lazy('transports details', kwargs={
            'pk': transport_id
        }))

@login_required
def reject_passenger_request(request, transport_id, user_id):
    current_transport = Transport.objects.filter(pk=transport_id).get()
    current_user = UserModel.objects.filter(pk=user_id).get()
    if request.method == 'POST':
        current_transport.requests.remove(current_user)
        current_transport.save()
        return redirect(reverse_lazy('transports details', kwargs={
            'pk': transport_id
        }))
@login_required
def create_chatroom(request, transport_id):
    current_transport = Transport.objects.filter(pk=transport_id).get()
    if request.method == 'POST':
        current_transport.chatroom_name = request.POST['chatroom_name']
        current_transport.save()
        return redirect(reverse_lazy('transports details', kwargs={
            'pk': transport_id
        }))