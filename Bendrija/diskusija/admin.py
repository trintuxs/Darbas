from django.contrib import admin
from diskusija.models import Diskusija, Komentaras, Balsavimas

# Register your models here.
admin.site.register(Diskusija)
admin.site.register(Komentaras)
admin.site.register(Balsavimas)