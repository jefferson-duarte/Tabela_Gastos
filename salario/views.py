from django.shortcuts import render
from .models import Salario


def salario(request):
    if request.method == 'POST':
        valor_salario = request.POST.get('salario')
        data_salario = request.POST.get('data')

        add_salario = Salario(
            salario=valor_salario,
            data=data_salario,
        )

        add_salario.save()

    return render(request, 'salario/salario.html')


def total_salario(request):
    sal = Salario.objects.all()

    val_sal = cont = 0
    while cont <= len(sal) - 1:
        val_sal += sal[cont].salario
        cont += 1

    context = {
        'salario': sal,
        'valor': val_sal,
    }

    return render(request, 'salario/salario.html', context)
