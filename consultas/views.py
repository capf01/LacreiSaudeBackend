from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ProfissionalSaude as Profissional, Cliente, Consulta


from .serializers import ProfissionalSerializer, ClienteSerializer, ConsultaSerializer

class ProfissionalListCreateView(APIView):
    """
    Endpoint para listar e criar profissionais.
    """
    def get(self, request):
        profissionais = Profissional.objects.all()
        serializer = ProfissionalSerializer(profissionais, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProfissionalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)