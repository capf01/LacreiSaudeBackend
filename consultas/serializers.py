from rest_framework import serializers
from .models import ProfissionalSaude, Consulta

class ProfissionalSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfissionalSaude
        fields = '__all__'

class ConsultaSerializer(serializers.ModelSerializer):
    profissional = serializers.SlugRelatedField(
        slug_field='nome_completo',
        queryset=ProfissionalSaude.objects.all()
    )

    class Meta:
        model = Consulta
        fields = '__all__'