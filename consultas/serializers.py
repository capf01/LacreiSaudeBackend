from rest_framework import serializers
from .models import ProfissionalSaude, Consulta

class ProfissionalSaudeSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo ProfissionalSaude.
    Utiliza o ModelSerializer para automatizar a criação dos campos com base no modelo.
    """
    class Meta:
        model = ProfissionalSaude
        # Especificando campos individuais para controle total (idealmente, especifique os campos)
        fields = ['id', 'nome_completo', 'especialidade', 'crm', 'telefone', 'email', 'endereco']

class ConsultaSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Consulta.
    Inclui a representação do profissional de saúde associado utilizando um campo slug.
    """
    # Representação do 'profissional' como nome completo (slug), para facilitar a leitura.
    profissional = serializers.SlugRelatedField(
        slug_field='nome_completo',  # Usamos o nome completo do profissional como referência
        queryset=ProfissionalSaude.objects.all(),  # Permite selecionar entre os profissionais cadastrados
        read_only=True  # Evita que o campo seja alterado diretamente
    )

    class Meta:
        model = Consulta
        # Especificando os campos que realmente queremos expor na serialização
        fields = ['id', 'cliente', 'profissional', 'data_agendamento', 'status']

    def validate_profissional(self, value):
        """
        Validação personalizada para garantir que o profissional realmente existe no banco de dados.
        """
        if not ProfissionalSaude.objects.filter(nome_completo=value).exists():
            raise serializers.ValidationError("Profissional não encontrado.")
        return value
