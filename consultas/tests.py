from django.urls import reverse
from rest_framework.test import APITestCase
from .models import ProfissionalSaude, Consulta

class ConsultaTests(APITestCase):
    def setUp(self):
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
        url = reverse('consulta-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)