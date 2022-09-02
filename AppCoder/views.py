from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Gerencia, Gerente, Colaborador
from EntregaIntermediaNaretto.AppCoder.forms import GerenciaFormulario, GerenteFormulario, ColaboradorFormulario

# Create your views here.

def gerencia(request):

      gerencia =  Gerencia(nombre="Gerencia General", n_integrantes="3")
      gerencia.save()
      documentoDeTexto = f"--->Gerencia: {gerencia.nombre}   Numero de Integrantes: {gerencia.n_integrantes}"

      return HttpResponse(documentoDeTexto)

def gerencias(request):

      if request.method == 'POST':

            miFormulario = GerenciaFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:   

                  informacion = miFormulario.cleaned_data

                  gerencia = Gerencia (nombre=informacion['gerencia'],  n_integrantes=informacion['n_integrantes']) 

                  gerencia.save()

                  return render(request, "AppCoder/inicio.html") 

      else: 

            miFormulario= GerenciaFormulario() 

      return render(request, "AppCoder/gerencias.html", {"miFormulario":miFormulario})

def gerentes(request):

      if request.method == 'POST':

            miFormulario = GerenteFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:   

                  informacion = miFormulario.cleaned_data
                  
                  gerente = Gerente (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], gerencia=informacion['gerencia']) 

                  gerente.save()

                  return render(request, "AppCoder/inicio.html") 

      else: 

            miFormulario= GerenteFormulario() 

      return render(request, "AppCoder/gerentes.html", {"miFormulario":miFormulario})

def colaboradores(request):

      if request.method == 'POST':

            miFormulario = ColaboradorFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data
                 
                  colaborador = Colaborador (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], cargo=informacion['cargo']) 

                  colaborador.save()

                  return render(request, "AppCoder/inicio.html")

      else: 

            miFormulario= ColaboradorFormulario()

      return render(request, "AppCoder/colaboradores.html", {"miFormulario":miFormulario})

def buscar(request):

      if  request.GET["apellido"]:

            apellido = request.GET["apellido"] 
            colaboradores = Colaborador.objects.filter(apellido__icontains=apellido)

            return render(request, "AppCoder/inicio.html", {"colaboradores":colaboradores, "apellido":apellido})

      else: 

            respuesta = "No enviaste los datos necesarios"

      return render(request,"AppCoder/inicio.html",{"respuesta":respuesta})