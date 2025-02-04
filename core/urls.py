from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from consultas.views import ProfissionalSaudeViewSet, ConsultaViewSet


router = DefaultRouter()
router.register(r'profissionais', ProfissionalSaudeViewSet)
router.register(r'consultas', ConsultaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]