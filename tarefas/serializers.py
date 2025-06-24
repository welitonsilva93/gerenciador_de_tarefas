from .models import Tarefas, Categoria
from rest_framework import serializers


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefas
        fields = '__all__'