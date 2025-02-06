from django.urls import path, include
from consultas.views import (
    ProfissionalListCreateView, ProfissionalDetailView,
    ClienteListCreateView, ClienteDetailView,
    AgendamentoCreateView, CancelamentoView
)

# Base URL da API (padrão para futuras versões)
BASE_API_PATH = 'api/v1/'

urlpatterns = [
    # ------------------------------------------------------------
    # Endpoints para Profissionais
    # ------------------------------------------------------------
    path(f'{BASE_API_PATH}profissionais/', ProfissionalListCreateView.as_view(), name='profissional-list-create'),
    path(f'{BASE_API_PATH}profissionais/<int:pk>/', ProfissionalDetailView.as_view(), name='profissional-detail'),

    # ------------------------------------------------------------
    # Endpoints para Clientes
    # ------------------------------------------------------------
    path(f'{BASE_API_PATH}clientes/', ClienteListCreateView.as_view(), name='cliente-list-create'),
    path(f'{BASE_API_PATH}clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),

    # ------------------------------------------------------------
    # Endpoints para Consultas
    # ------------------------------------------------------------
    path(f'{BASE_API_PATH}consultas/agendar/', AgendamentoCreateView.as_view(), name='agendamento-create'),
    path(f'{BASE_API_PATH}consultas/cancelar/<int:pk>/', CancelamentoView.as_view(), name='cancelamento'),

    # ------------------------------------------------------------
    # Possível expansão futura
    # ------------------------------------------------------------
    # path(f'{BASE_API_PATH}outro_recurso/', include('outra_app.urls')),
]
