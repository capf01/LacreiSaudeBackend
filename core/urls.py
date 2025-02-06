# Atualização do Backend - Lacrei Saúdefrom django.urls import path
from consultas.views import (
    ProfissionalListCreateView, ProfissionalDetailView,
    ClienteListCreateView, ClienteDetailView,
    AgendamentoCreateView, CancelamentoView
)

urlpatterns = [
    path('profissionais/', ProfissionalListCreateView.as_view(), name='profissional-list-create'),
    path('profissionais/<int:pk>/', ProfissionalDetailView.as_view(), name='profissional-detail'),
    path('clientes/', ClienteListCreateView.as_view(), name='cliente-list-create'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
    path('consultas/agendar/', AgendamentoCreateView.as_view(), name='agendamento-create'),
    path('consultas/cancelar/<int:pk>/', CancelamentoView.as_view(), name='cancelamento')
]