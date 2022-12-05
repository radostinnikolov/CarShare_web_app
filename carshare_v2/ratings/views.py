from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from carshare_v2.ratings.models import Rating


def rate_user(request, giver_id, receiver_id):
    if request.method == 'POST':
        Rating.objects.create(from_profile_id=giver_id, to_profile_id=receiver_id, value=request.POST['rating'])
        return redirect(reverse_lazy('profile details', kwargs={
            'pk':receiver_id
        }))