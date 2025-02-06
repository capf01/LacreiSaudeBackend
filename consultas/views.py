from django.shortcuts import get_object_or_404 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import ProfissionalSaude as Profissional, Cliente, Consulta
from .serializers import ProfissionalSerializer, ClienteSerializer, ConsultaSerializer
from rest_framework import status

class ProfissionalListCreateView(APIView):
    """
    Endpoint para listar todos os profissionais de saúde cadastrados e criar novos registros.
    """
    permission_classes = [IsAuthenticated]  # Permite apenas usuários autenticados

    def get(self, request):
        try:
            # Obtém todos os registros de profissionais do banco de dados.
            profissionais = Profissional.objects.all()
            # Serializa os dados.
            serializer = ProfissionalSerializer(profissionais, many=True)
            # Retorna a lista de profissionais.
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            # Recebe e serializa os dados enviados para criar um novo profissional.
            serializer = ProfissionalSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()  # Salva o novo profissional
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            # Caso a validação falhe, retorna os erros.
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
