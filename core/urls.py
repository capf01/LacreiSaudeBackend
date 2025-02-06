# Atualização do Backend - Lacrei Saúde
# Este arquivo define as URLs que mapeiam para as views responsáveis por gerenciar profissionais,
# clientes e operações de consultas (agendamento e cancelamento).
# Comentários estratégicos foram adicionados para facilitar o entendimento e futuras manutenções.

from django.urls import path
from consultas.views import (
    ProfissionalListCreateView, ProfissionalDetailView,
    ClienteListCreateView, ClienteDetailView,
    AgendamentoCreateView, CancelamentoView
)

urlpatterns = [
    # ------------------------------------------------------------
    # Endpoints para profissionais
    # ------------------------------------------------------------
    # 'profissionais/': Permite listar todos os profissionais cadastrados
    # e criar um novo profissional.
    path('profissionais/', ProfissionalListCreateView.as_view(), name='profissional-list-create'),
    
    # 'profissionais/<int:pk>/': Permite acessar os detalhes de um profissional específico
    # (identificado pelo 'pk') para visualização, atualização ou exclusão.
    path('profissionais/<int:pk>/', ProfissionalDetailView.as_view(), name='profissional-detail'),
    
    # ------------------------------------------------------------
    # Endpoints para clientes
    # ------------------------------------------------------------
    # 'clientes/': Permite listar todos os clientes cadastrados
    # e criar um novo cliente.
    path('clientes/', ClienteListCreateView.as_view(), name='cliente-list-create'),
    
    # 'clientes/<int:pk>/': Permite acessar os detalhes de um cliente específico
    # (identificado pelo 'pk') para visualização, atualização ou exclusão.
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
    
    # ------------------------------------------------------------
    # Endpoints para operações de consultas
    # ------------------------------------------------------------
    # 'consultas/agendar/': Endpoint para agendamento de uma nova consulta.
    # A lógica de criação do agendamento é tratada pela view AgendamentoCreateView.
    path('consultas/agendar/', AgendamentoCreateView.as_view(), name='agendamento-create'),
    
    # 'consultas/cancelar/<int:pk>/': Endpoint para cancelamento de uma consulta existente.
    # O 'pk' identifica univocamente o agendamento que deverá ser cancelado.
    path('consultas/cancelar/<int:pk>/', CancelamentoView.as_view(), name='cancelamento')
]
