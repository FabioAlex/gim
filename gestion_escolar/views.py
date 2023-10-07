from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
import datetime
from django.template import Template, Context
from .forms import DocenteForm

def crear_docente(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            docente = form.save()
            return redirect('detalles_docente', docente_id=docente.id)
    else:
        form = DocenteForm()
    
    return render(request, 'crear_docente.html', {'form': form})

def pagina1(request):
    plantillaExterna = open("C:\Users\Desarrollo\Documents\Proyecto Gimnasio\mysite\gim\gestion_escolar\templates\pagina1.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)
    