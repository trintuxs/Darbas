from django.urls import path
from . import views


urlpatterns = [
    path('flat/', views.flat, name='butas'),
    path('', views.index, name='index'),
    path('resident/', views.residents, name='gyventojas_list'),
    path('resident-list/', views.ResidentListView.as_view(), name='gyventojas'),

]



#path('register/', views.register, name='register'),
#path('prisijungti/', views.prisijungimas, name='prisijungti'),