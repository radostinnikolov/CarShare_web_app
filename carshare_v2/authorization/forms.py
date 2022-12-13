from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from carshare_v2.accounts.models import Profile

UserModel = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = UserModel
        fields = (
            'email', 'password1', 'password2', 'first_name', 'last_name')
        help_texts = {
            'email': 'Enter a valid email address.'
        }



    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            user=user,
        )
        if commit:
            profile.save()

        return user


