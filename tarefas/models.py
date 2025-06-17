from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    titulo_cat = models.CharField(max_length=60)

    def __str__(self):
        return self.titulo_cat


class Tarefas(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=200)
    data_criacao = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.titulo