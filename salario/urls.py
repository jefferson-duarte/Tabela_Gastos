from django.urls import path
from . import views

urlpatterns = [
    path('', views.salario, name='index'),
    # path('total/', views.total_salario, name='total'),
]
