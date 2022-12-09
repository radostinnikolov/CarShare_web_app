from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model


from carshare_v2.accounts.models import Profile


UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'last_login', 'date_joined', 'is_superuser', 'is_staff')
    list_filter = ('id', 'is_superuser', 'is_staff')
    search_fields = ('id', 'is_superuser', 'is_staff')
    sortable_by = ('id', 'is_superuser', 'is_staff')
    ordering = ('date_joined',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_name', 'last_name')
    list_filter = ('user_id', 'first_name', 'last_name')
    search_fields = ('user_id', 'first_name', 'last_name')
    sortable_by = ('user_id', 'first_name', 'last_name')
    ordering = ('user_id',)
