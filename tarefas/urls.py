from django.contrib import admin
from django.urls import path, include
from . import views
from.views import CriarTarefaView, ExcluirTarefaView, MostrarTarefasView


urlpatterns = [
    path('', MostrarTarefasView.as_view(), name='ver_tarefa'),
    path('criar', CriarTarefaView.as_view(), name='criar_tarefa'),
    path('delete_tarefa/<int:i>/', ExcluirTarefaView.as_view(), name='delete_tarefa'),
    path('update_tarefa/<int:id>/', views.update_tarefa, name='update_tarefa')
]
