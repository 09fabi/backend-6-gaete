from django.shortcuts import render, redirect
from App_6.models import Proyecto
from App_6.forms import ProyectoForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def listado(request):
    proye = Proyecto.objects.all()
    data = {'proyec': proye}
    return render(request, 'listado.html', data)


def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'listado.html')
    else:
        form = ProyectoForm()

    return render(request, 'form_proyecto.html', {'form': form})
