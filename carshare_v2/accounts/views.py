from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from carshare_v2.accounts.models import Profile
from carshare_v2.comments.models import Comment
from carshare_v2.common.views import IndexView
from carshare_v2.friends.models import FriendRequest, Friend
from carshare_v2.ratings.models import Rating

UserModel = get_user_model()


class ProfileDetailsView(LoginRequiredMixin, generic.DetailView):
    template_name = 'accounts/profile-details.html'
    model = UserModel


    def get_commenters_ids(self):
        return [x.from_profile_id for x in Comment.objects.filter(to_profile_id=self.object.pk)]

    def get_raters_ids(self):
        return [x.from_profile_id for x in Rating.objects.filter(to_profile_id=self.object.pk)]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_sent_friend_request'] = self.request.user.pk in IndexView.get_requesters_ids(self.object.pk)
        context['has_commented'] = self.request.user.pk in self.get_commenters_ids()
        context['has_rated'] = self.request.user.pk in self.get_raters_ids()
        context['rating'] = sum(x.value for x in Rating.objects.filter(to_profile_id=self.object.pk).all())
        context['comments'] = Comment.objects.filter(to_profile_id=self.object.pk).all()
        if context['has_commented']:
            context['current_comment'] = Comment.objects.filter(to_profile_id=self.object.pk, from_profile_id=self.request.user.pk).get()
        context['is_friend'] = self.request.user.pk in IndexView.get_friends_ids(self.object.pk)
        context['friend_request_users'] = UserModel.objects.filter(id__in=IndexView.get_requesters_ids(self.object.pk))
        context['friend_users'] = UserModel.objects.filter(id__in=IndexView.get_friends_ids(self.object.pk))
        return context


class ProfileEditView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'accounts/profile-edit.html'
    model = Profile
    fields = ['first_name', 'last_name', 'age', 'description', 'profile_picture']

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={
            'pk': self.request.user.pk,
        })


class ProfileDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'accounts/profile-delete.html'
    model = UserModel
    success_url = reverse_lazy('index')
