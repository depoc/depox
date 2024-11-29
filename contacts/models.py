from django.db import models

from erp.models import Company


class Contacts(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    nome = models.CharField(max_length=255)
    apelido = models.CharField(max_length=255, blank=True)    
    pessoa = models.CharField(max_length=255)
    cpf_cnpj = models.CharField(max_length=18, unique=True)
    contribuinte = models.CharField(max_length=255, blank=True)
    ie = models.IntegerField()
    im = models.IntegerField()
    tipo = models.CharField(max_length=255)
    status = models.CharField(max_length=255, blank=True)

    celular = models.CharField(max_length=14, blank=True)
    email = models.EmailField(blank=True)

    endereco = models.CharField(max_length=255, blank=True)
    numero = models.PositiveIntegerField(blank=True)
    bairro = models.CharField(max_length=255, blank=True)
    complemento = models.CharField(max_length=255, blank=True)
    cidade = models.CharField(max_length=255, blank=True)
    uf = models.CharField(max_length=2, blank=True)    
    cep = models.CharField(max_length=9, blank=True)

    nascimento = models.DateField()
    observacoes = models.CharField(max_length=255, blank=True)
    anexos = models.FileField(upload_to='media/anexos')