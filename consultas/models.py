from django.db import models

class ProfissionalSaude(models.Model):
    nome_completo = models.CharField(max_length=200)
    profissao = models.CharField(max_length=100)
    endereco = models.TextField()
    contato = models.CharField(max_length=100)
    nome_social = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome_completo

class Consulta(models.Model):
    data = models.DateTimeField()
    profissional = models.ForeignKey(ProfissionalSaude, on_delete=models.CASCADE)

    def __str__(self):
        return f"Consulta com {self.profissional.nome_completo} em {self.data}"