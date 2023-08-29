from django.urls import path
from . import views

urlpatterns = [
    path('', views.visos_diskusijos, name='visos_diskusijos'),
    path('<int:diskusija_id>/', views.diskusija_detail, name='diskusija_detail'),
    path('<int:diskusija_id>/balsuoti/', views.balsuoti_diskusija, name='balsuoti_diskusija'),
    path('<int:diskusija_id>/prideti_komentara/', views.prideti_komentara, name='prideti_komentara'),
    path('kurti_diskusija/', views.kurti_diskusija, name='kurti_diskusija'),

]
