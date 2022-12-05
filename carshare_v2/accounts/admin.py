from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model


from carshare_v2.accounts.models import Profile


UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
