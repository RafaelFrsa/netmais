from django.urls import path, include
from .views import *

urlpatterns = [

    path('equipamentos/', EquipamentsList.as_view(), name='equipaments_list'),
    path('equipamentos/<int:pk>/', EquipamentsDetail.as_view(), name='equipaments_detail'),
    path('equipamentos/update/<int:pk>/', EquipamentsUpdate.as_view(), name='equipaments_update'),
    path('equipamentos/delete/<int:pk>/', EquipamentsDelete.as_view(), name='equipaments_delete'),
    path('equipamentos/cadastrar/', EquipamentsCreate.as_view(), name='equipaments_create'),

    path('clientes', ClientsList.as_view(), name='clients_list'),
    path('cliente/<int:pk>/', ClientsDetail.as_view(), name='clients_detail'),
    path('cliente/update/<int:pk>/', ClientsUpdate.as_view(), name='clients_update'),
    path('cliente/delete/<int:pk>/', ClientsDelete.as_view(), name='clients_delete'),
    path('cliente/cadastrar/', ClientsCreate.as_view(), name='clients_create'),    
]
