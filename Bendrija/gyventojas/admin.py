from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from gyventojas.forms import CustomUserCreationForm, CustomUserChangeForm
from gyventojas.models import Resident, Flat


class FlatAdmin(admin.ModelAdmin):
    list_display = ('flat_nr', 'size_kv', 'owner')


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Resident
    list_display = ["first_name", "last_name", "email", "flat_nr"]

    fieldsets = UserAdmin.fieldsets + (
        (
            'Flat information',
            {
                'fields': (
                    'flat_nr',
                ),
            },
        ),
    )


# Register your models here.
admin.site.register(Resident, CustomUserAdmin)

admin.site.register(Flat, FlatAdmin)
# admin.site.register(ResidentAdmin)



