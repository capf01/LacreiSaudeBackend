from django.urls import reverse 
from rest_framework.test import APITestCase
from .models import ProfissionalSaude, Consulta

class ConsultaTests(APITestCase):
    """
    Testes para o endpoint de consultas.
    Utilizamos APITestCase do Django REST Framework para facilitar a criação de testes integrados.
    """

    def setUp(self):
        """
        Método de configuração executado antes de cada teste.
        Cria instâncias necessárias:
        - Um profissional de saúde para associar à consulta.
        - Uma consulta, utilizando o profissional criado.
        Isso garante um ambiente de teste controlado e previsível.
        """
        self.profissional = ProfissionalSaude.objects.create(
            nome_completo="Dr. João Silva",
            profissao="Cardiologista",
            endereco="Rua das Flores, 123",
            contato="(11) 99999-9999"
        )
        self.consulta = Consulta.objects.create(
            data="2023-10-01T10:00:00Z",
            profissional=self.profissional
        )

    def test_list_consultas(self):
        """
        Testa a listagem de consultas através do endpoint 'consulta-list'.
        Verifica se:
        - O endpoint retorna um status HTTP 200 (OK).
        - O número de consultas retornadas corresponde ao esperado (neste caso, 1).
        """
        # Obtém a URL do endpoint utilizando o nome definido no arquivo de rotas (reverse lookup)
        url = reverse('consulta-list')
        # Realiza uma requisição GET para o endpoint
        response = self.client.get(url)
        # Assegura que a resposta tenha status HTTP 200
        self.assertEqual(response.status_code, 200)
        # Verifica se exatamente uma consulta foi retornada
        self.assertEqual(len(response.data), 1)
