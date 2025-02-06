from django.db import models

from django.db import models

class ProfissionalSaude(models.Model):
    # Nome completo do profissional, usado para identificação em listas e visualizações.
    nome_completo = models.CharField(max_length=200)
    # Profissão do profissional, como "Médico", "Enfermeiro", etc.
    profissao = models.CharField(max_length=100)
    # Endereço completo, permitindo detalhes extensos sobre localização.
    endereco = models.TextField()
    # Contato para comunicação, pode incluir telefone, e-mail ou outros meios.
    contato = models.CharField(max_length=100)
    # Nome social, campo opcional para registro de nome preferido ou utilizado socialmente.
    nome_social = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        # Retorna o nome completo para uma representação legível do objeto, útil em painéis administrativos.
        return self.nome_completo

class Consulta(models.Model):
    # Data e hora marcadas para a consulta, utilizando DateTimeField para capturar ambas as informações.
    data = models.DateTimeField()
    # Associação com o profissional de saúde responsável pela consulta.
    # O parâmetro on_delete=models.CASCADE garante que, se o profissional for removido,
    # as consultas associadas também sejam excluídas, mantendo a integridade dos dados.
    profissional = models.ForeignKey(ProfissionalSaude, on_delete=models.CASCADE)

    def __str__(self):
        # Retorna uma string descritiva da consulta, incluindo o nome do profissional e a data agendada,
        # facilitando a identificação e a leitura em logs ou interfaces administrativas.
        return f"Consulta com {self.profissional.nome_completo} em {self.data}"
