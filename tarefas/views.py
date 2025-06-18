from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormularioTarefa
from django.urls import reverse
from . models import Tarefas, Categoria
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def ver_tarefa(request):
    categoria_id = request.GET.get('categoria')
    usuario_id = request.GET.get('usuario')

    tarefas = Tarefas.objects.all().order_by('titulo')

    if categoria_id:
        tarefas = tarefas.filter(categoria_id=categoria_id)

    if usuario_id:
        tarefas = tarefas.filter(usuario_id=usuario_id)

    categorias = Categoria.objects.all()
    usuario = User.objects.all()
    context = {
        'tarefas': tarefas,
        'categorias': categorias,
        'usuario': usuario,
        'categoria_selecionada': categoria_id,
        'usuario_selecionado': usuario_id,
    }
    return render(request, 'tarefas/home_tarefa.html', context)

@login_required
def criar_tarefa(request):
    if request.method == 'POST':
        form = FormularioTarefa(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.usuario = request.user
            tarefa.save()
            messages.success(request, "Tarefa criada com sucesso!")
            return redirect(reverse('ver_tarefa'))

    else:
        form = FormularioTarefa()

    return render(request, 'tarefas/criar_tarefa.html', {'form': form})

@login_required
def delete_tarefa(request, i):
    task_tarefas = Tarefas.objects.get(id=i)

    task_tarefas.delete()
    messages.success(request, "Tarefa removida com sucesso!")
    return redirect(reverse('ver_tarefa'))

@login_required
def update_tarefa(request, id):
    task_tarefas = get_object_or_404(Tarefas, id=id)

    if request.method ==  'POST':
        form = FormularioTarefa(request.POST, instance=task_tarefas)

        if form.is_valid():
            form.save()
            messages.success(request, "Tarefa atualizada com sucesso!")
            return redirect('ver_tarefa')
        
    else:
        form = FormularioTarefa(instance=task_tarefas)

    return render(request, 'tarefas/editar_tarefa.html', {'form': form})