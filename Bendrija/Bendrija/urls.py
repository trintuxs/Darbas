from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin


from django.urls import path, include

urlpatterns = [
                  path('', include('gyventojas.urls')),
                  path('admin/', admin.site.urls),
                  path('administracija/', include('administracija.urls')),
                  path('diskusija/', include('diskusija.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
              ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)