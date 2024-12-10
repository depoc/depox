from django.db import models

from erp.models import Company


class Contacts(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='contacts')
    created = models.DateTimeField(auto_now_add=True)

    nome = models.CharField(max_length=255)
    apelido = models.CharField(max_length=255, blank=True)    
    pessoa = models.CharField(max_length=255)
    cpf_cnpj = models.CharField(max_length=18, unique=True)
    contribuinte = models.CharField(max_length=255, blank=True)
    ie = models.IntegerField(blank=True, null=True)
    im = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255, blank=True, default='ativo')

    celular = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)

    endereco = models.CharField(max_length=255, blank=True)
    numero = models.PositiveIntegerField(blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True)
    complemento = models.CharField(max_length=30, blank=True)
    cidade = models.CharField(max_length=255, blank=True)
    uf = models.CharField(max_length=2, blank=True)    
    cep = models.CharField(max_length=9, blank=True)

    nascimento = models.DateField(blank=True, null=True)
    observacoes = models.CharField(max_length=255, blank=True)
    anexos = models.FileField(upload_to='media/anexos', blank=True, null=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome']