from django.urls import path, include
from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='equipamentos/equipamentos.html'), name='home'),
    path('clientes', ClientsList.as_view(), name='clients_list'),
    path('cliente/<int:pk>/', ClientsDetail.as_view(), name='clients_detail'),
    path('cliente/update/<int:pk>/', ClientsUpdate.as_view(), name='clients_update'),
    path('cliente/delete/<int:pk>/', ClientsDelete.as_view(), name='clients_delete'),
    path('cliente/cadastrar/', ClientsCreate.as_view(), name='clients_create'),
    path('equipamentos/listar', EquipamentsList.as_view()),
]
