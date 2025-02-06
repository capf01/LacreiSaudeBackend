from rest_framework import serializers
from .models import ProfissionalSaude, Consulta

class ProfissionalSaudeSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo ProfissionalSaude.
    Utiliza o ModelSerializer para automatizar a criação dos campos com base no modelo.
    """
    class Meta:
        # Define o modelo que será serializado.
        model = ProfissionalSaude
        # Utiliza todos os campos do modelo. Em projetos futuros, pode ser interessante especificar campos individualmente.
        fields = '__all__'

class ConsultaSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Consulta.
    Inclui a representação do profissional de saúde associado utilizando um campo slug.
    """
    # O campo 'profissional' é representado pelo nome completo do profissional,
    # facilitando a leitura e evitando a exposição do ID interno.
    profissional = serializers.SlugRelatedField(
        slug_field='nome_completo',  # Campo do modelo ProfissionalSaude que será exibido.
        queryset=ProfissionalSaude.objects.all()  # Permite a seleção do profissional a partir de todos os registros.
    )

    class Meta:
        # Define o modelo que será serializado.
        model = Consulta
        # Inclui todos os campos do modelo na serialização. Avalie, no futuro, se é necessário expor todos os campos.
        fields = '__all__'
