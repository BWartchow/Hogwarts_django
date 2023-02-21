from django.urls import path
from . import views

app_name = 'sonserina'
urlpatterns = [
    path('', views.salao_comunal, name='salao_comunal'),  # home
    path('sobre', views.sobre, name='sobre'),  # sobre
    path('membros', views.membros, name='membros'),  # membros
    path('quadribol', views.quadribol, name='quadribol'),  # quadribol
    path('quadribol/trofeu/<int:id>', views.trofeu, name='trofeu'),  # quadribol
]
