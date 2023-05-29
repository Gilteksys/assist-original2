from django.urls import path
from contatos import views

urlpatterns = [    
    path('cliente_create/', views.cliente_create, name='cliente_create'),
    path('cliente_list/', views.cliente_list, name='cliente_list'),
    path('buscar_cliente_por_nome/', views.buscar_cliente_por_nome, name='buscar_cliente_por_nome'),
    path('ordem_servico_create/', views.ordem_servico_create, name='orden_servico_create'),   
]
