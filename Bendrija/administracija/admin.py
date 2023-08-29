from django.contrib import admin

from administracija.models import Kaupiamasis_Inasas, Expenses, Staff

# Register your models here.
admin.site.register(Kaupiamasis_Inasas)
admin.site.register(Expenses)
admin.site.register(Staff)
