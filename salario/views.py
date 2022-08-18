from django.shortcuts import render, get_object_or_404, redirect
from .models import Salario
from django.contrib import messages


def salario(request):
    try:
        if request.method == 'POST':
            valor_salario = request.POST.get('salario')
            data_salario = request.POST.get('data')

            add_salario = Salario(
                salario=valor_salario,
                data=data_salario,
            )

            add_salario.save()
    except:  # noqa
        messages.add_message(
            request,
            messages.ERROR,
            'ERRO. Informe apenas valores válidos. Ex.(999.99)'
        )

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


def salario_editar(request, id):
    ...


def salario_deletar(request, pk):
    salario = get_object_or_404(Salario, pk=pk)
    salario.delete()

    return redirect('index')
