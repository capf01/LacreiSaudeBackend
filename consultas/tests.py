from django.urls import reverse
from rest_framework.test import APITestCase
from .models import ProfissionalSaude, Consulta
from rest_framework import status

class ConsultaTests(APITestCase):
    """
    Testes para o endpoint de consultas.
    Utilizado APITestCase do Django REST Framework para facilitar a criação de testes integrados.
    """

    def setUp(self):
        """
        Método de configuração executado antes de cada teste.
        Cria instâncias necessárias para garantir um ambiente de teste controlado.
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
        self.url = reverse('consulta-list')  # URL para o endpoint de listagem de consultas

    def test_list_consultas(self):
        """
        Testa a listagem de consultas através do endpoint 'consulta-list'.
        Verifica se o status HTTP 200 é retornado e se os dados são corretos.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Verifica se há 1 consulta
        self.assertEqual(response.data[0]['profissional'], "Dr. João Silva")  # Verifica o nome do profissional

    def test_create_consulta(self):
        """
        Testa a criação de uma nova consulta através do endpoint 'consulta-list'.
        Verifica se o status HTTP 201 (Created) é retornado e se a consulta foi criada corretamente.
        """
        data = {
            "data": "2023-10-15T14:00:00Z",
            "profissional": self.profissional.nome_completo  # Usando nome completo do profissional
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['data'], "2023-10-15T14:00:00Z")  # Verifica se a data está correta
        self.assertEqual(response.data['profissional'], "Dr. João Silva")  # Verifica o nome do profissional

    def test_delete_consulta(self):
        """
        Testa a exclusão de uma consulta existente através do endpoint 'consulta-detail'.
        Verifica se o status HTTP 204 (No Content) é retornado.
        """
        # URL do endpoint para excluir uma consulta
        url = reverse('consulta-detail', args=[self.consulta.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Verifica se a consulta foi realmente excluída
        self.assertEqual(Consulta.objects.count(), 0)  # Nenhuma consulta deve existir após a exclusão
