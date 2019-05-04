from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from users.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        (None, {
            "fields": (
                'email',
                'password'
            ),
        }),
    )
    limited_fieldsets = (
        (None, {
            'fields': (
                'email',
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email',
                       'password1', 'password2', 'send_email_for_downtime',
                       'send_email_for_issues')}
         ),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = auth_admin.AdminPasswordChangeForm
    list_display = ('email', 'first_name', 'last_name', 'is_superuser')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('id',)
    list_filter = ('first_name', 'last_name', 'email')
    filter_horizontal = ()
    readonly_fields = ('last_login', 'date_joined',)


admin.site.register(User, UserAdmin)
