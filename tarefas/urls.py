from django.contrib import admin
from django.urls import path, include
from . import views
from.views import *


urlpatterns = [
    path('', MostrarTarefasView.as_view(), name='ver_tarefa'),
    path('criar', CriarTarefaView.as_view(), name='criar_tarefa'),
    path('delete_tarefa/<int:i>/', ExcluirTarefaView.as_view(), name='delete_tarefa'),
    path('update_tarefa/<int:pk>/', AtualizarTarefaView.as_view(), name='update_tarefa')
]
