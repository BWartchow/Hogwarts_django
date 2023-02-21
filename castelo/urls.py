from django.urls import path
from . import views

app_name = 'castelo'
urlpatterns = [
    path('', views.castelo, name='home'),  # home
    path('casas/', views.casas, name='casas'),  # casas
]
