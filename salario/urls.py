from django.urls import path
from . import views

urlpatterns = [
    path('', views.salario, name='index'),
    path('editar/<int:pk>/', views.salario_editar, name='editar'),
    path('deletar/<int:pk>/', views.salario_deletar, name='deletar'),
]
