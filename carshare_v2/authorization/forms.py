from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms


from carshare_v2.accounts.models import Profile

UserModel = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    # age = forms.IntegerField()
    # profile_picture = forms.ImageField()
    # description = forms.Textarea()

    class Meta:
        model = UserModel
        fields = (
            UserModel.USERNAME_FIELD, 'password1', 'password2', 'first_name', 'last_name')
        # 'age', 'profile_picture', 'description'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            # age=self.cleaned_data['age'],
            # profile_picture=self.cleaned_data['profile_picture'],
            # description=self.cleaned_data['description'],
            user=user,
        )
        if commit:
            profile.save()

        return user


