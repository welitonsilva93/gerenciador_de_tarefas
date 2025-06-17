from django import forms
from .models import *

class FormularioTarefa(forms.ModelForm):

    class Meta:
        model = Tarefas
        fields = ['titulo', 'descricao', 'categoria']