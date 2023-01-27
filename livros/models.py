from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=30,null=True)
    descricao = models.TextField(null=True)

    class Meta:
        ordering = ['nome']

    def __str__(self) -> str:
        return self.nome

class Livro(models.Model):
    Titulo = models.CharField("Título", max_length = 100)
    Codigo = models.CharField("Código", max_length = 20, null = True)
    Autor = models.CharField(max_length = 100)
    Coautor = models.CharField(blank = True, max_length = 100)
    Edicao = models.IntegerField("Edição") 
    Volume = models.IntegerField(null = True)
    state_choices = (
        ('Bem conservado','Bem conservado'),
        ('Conservado','Conservado'),
        ('Pouco conservado','Pouco conservado')
    )
    Estado = models.CharField(max_length = 30, null = True, choices = state_choices)
    type_choices = (
        ('Livro','Livro'),
        ('Cópia','Cópia')
    )
    Tipo = models.CharField(max_length = 30, null = True, choices = type_choices)
    Data = models.DateField(null = True)
    Categoria = models.ForeignKey(Categoria, on_delete = models.SET_NULL,null=True)

    class Meta:
        ordering = ['Titulo','Autor']

    def __str__(self) -> str:
        return self.Titulo