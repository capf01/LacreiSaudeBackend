from django.shortcuts import get_object_or_404 
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ProfissionalSaude as Profissional, Cliente, Consulta
from .serializers import ProfissionalSerializer, ClienteSerializer, ConsultaSerializer

class ProfissionalListCreateView(APIView):
    """
    Endpoint para listar todos os profissionais de saúde cadastrados e criar novos registros.
    A utilização de uma única classe para GET e POST centraliza a lógica, facilitando futuras modificações.
    """
    def get(self, request):
        # Obtém todos os registros de profissionais do banco de dados.
        profissionais = Profissional.objects.all()
        # Serializa os dados, convertendo os objetos do Django para um formato compatível (geralmente JSON).
        serializer = ProfissionalSerializer(profissionais, many=True)
        # Retorna a lista de profissionais com status HTTP 200 (OK).
        return Response(serializer.data)
    
    def post(self, request):
        # Recebe e serializa os dados enviados na requisição para criar um novo profissional.
        serializer = ProfissionalSerializer(data=request.data)
        # Valida os dados enviados. Se os dados forem válidos, o novo registro é salvo no banco de dados.
        if serializer.is_valid():
            serializer.save()  # Salva os dados e realiza qualquer processamento adicional definido no serializer.
            # Retorna os dados do profissional criado com status HTTP 201 (Created).
            return Response(serializer.data, status=201)
        # Caso a validação falhe, retorna os erros com status HTTP 400 (Bad Request).
        return Response(serializer.errors, status=400)
