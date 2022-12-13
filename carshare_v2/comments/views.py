from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from carshare_v2.comments.models import Comment

@login_required
def create_new_comment(request, commenter_id, commented_id):
    if request.method == 'POST':
        Comment.objects.create(from_profile_id=commenter_id, to_profile_id=commented_id,
                               content=request.POST['w3review'])
        return redirect(reverse_lazy('profile details', kwargs={
            'pk': commented_id
        }))

@login_required
def delete_comment(request, commenter_id, commented_id):
    if request.method == 'POST':
        Comment.objects.filter(from_profile_id=commenter_id, to_profile_id=commented_id).get().delete()
        return redirect(reverse_lazy('profile details', kwargs={
            'pk': commented_id
        }))
