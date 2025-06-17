from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ver_tarefa, name='ver_tarefa'),
    path('criar', views.criar_tarefa, name='criar_tarefa'),
    path('delete_tarefa/<int:i>/', views.delete_tarefa, name='delete_tarefa'),
    path('update_tarefa/<int:id>/', views.update_tarefa, name='update_tarefa')
]
