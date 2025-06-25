from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormularioTarefa
from django.urls import reverse, reverse_lazy
from . models import Tarefas, Categoria
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView

from rest_framework import viewsets
from .serializers import TarefaSerializer

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefas.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Tarefas.objects.all()
        categoria = self.request.query_params.get('categoria')
        usuario = self.request.query_params.get('usuario')

        if categoria:
            queryset = queryset.filter(categoria_id=categoria)
        if usuario:
            queryset = queryset.filter(usuario_id=usuario)

        return queryset.order_by('titulo')
    

class CriarTarefaView(LoginRequiredMixin, CreateView):
    model = Tarefas
    form_class = FormularioTarefa
    template_name = 'tarefas/criar_tarefa.html'
    success_url = reverse_lazy('ver_tarefa')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        messages.success(self.request, "Tarefa criada com sucesso!")
        return super().form_valid(form)


class ExcluirTarefaView(LoginRequiredMixin, DeleteView):
    model = Tarefas
    success_url = reverse_lazy('ver_tarefa')

    def get(self, request, *args, **kwargs):
        obj = self.get_object
        obj.delete()
        messages.success(request, "Tarefa removida com sucesso!")
        return super().delete(request, *args, **kwargs)

class MostrarTarefasView(LoginRequiredMixin, ListView):
    model = Tarefas
    template_name = 'tarefas/home_tarefa.html'
    context_object_name = 'tarefas'
    ordering = ['titulo']

    def get_queryset(self):
        queryset = Tarefas.objects.all()
        categoria_id = self.request.GET.get('categoria')
        usuario_id = self.request.GET.get('usuario')

        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)

        if usuario_id:
            queryset = queryset.filter(usuario_id=usuario_id)

        return queryset.order_by('titulo')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['usuarios'] = User.objects.all()
        context['categoria_selecionada'] = self.request.GET.get('categoria')
        context['usuario_selecionado'] = self.request.GET.get('usuario')
        return context


class AtualizarTarefaView(LoginRequiredMixin, UpdateView):

    model = Tarefas
    template_name = 'tarefas/editar_tarefa.html'
    form_class = FormularioTarefa
    success_url = reverse_lazy('ver_tarefa')

    def form_valid(self, form):
        messages.success(self.request, "Tarefa atualizada com sucesso!")
        return super().form_valid(form)
    