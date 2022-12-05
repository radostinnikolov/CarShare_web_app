from django import forms

from carshare_v2.friends.models import FriendRequest, Friend


class BaseFriendRequestForm(forms.ModelForm):
    class Meta:
        model = FriendRequest
        fields = ()


class BaseFriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ()
