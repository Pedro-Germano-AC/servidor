from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=30,null=True)
    descricao = models.TextField(null=True)

    class Meta:
        ordering = ['nome']

    def __str__(self) -> str:
        return self.nome

class Livro(models.Model):
    Disponivel = models.BooleanField(null=True)
    Titulo = models.CharField("Título", max_length = 100, null = True)
    Codigo = models.CharField("Código", max_length = 20, null = True)
    Autores = models.CharField(max_length = 100, null = True)
    Edicao = models.IntegerField("Edição", null = True, default=0)	
    Volume = models.IntegerField(null = True, default=0)
    state_choices = (
        ('Bem conservado','Bem conservado'),
        ('Conservado','Conservado'),
        ('Pouco conservado','Pouco conservado')
    )
    Estado = models.CharField(max_length = 30, choices = state_choices, null = True)
    type_choices = (
        ('Livro','Livro'),
        ('Cópia','Cópia')
    )
    Tipo = models.CharField(max_length = 30, choices = type_choices, default = 'Livro', null = True)
    Categoria = models.ForeignKey(Categoria, on_delete = models.SET_NULL,null=True)

    class Meta:
        ordering = ['Disponivel', 'Titulo','Autores']

    def __str__(self) -> str:
        return self.Titulo

class Emprestimo(models.Model):
    Livro = models.ForeignKey(Livro, on_delete = models.SET_NULL, null = True)
    Usuario = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    Nome = models.CharField("Nome do usuário", max_length = 100, null = True)
    Matricula = models.CharField("Matrícula do usuário", max_length = 20, null = True)
    Telefone = models.CharField("Telefone do usuário", max_length = 20, null = True)
    DataEmprestimo = models.DateField("Data do empréstimo", null = True)
    DataRecebimento = models.DateField("Data do recebimento estimado", null = True, )
    DataDevolucaoEstimado = models.DateField( "Data da devolução estimada", null = True)
    DataDevolucaoReal = models.DateField("Data da devolução real", null = True)
    Recebido = models.BooleanField(null = True, default = True)

