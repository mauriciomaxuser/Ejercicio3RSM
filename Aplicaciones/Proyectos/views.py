from django.shortcuts import render,redirect
from .models import Proyecto,Desarrollador
from django.contrib import messages

# Create your views here.
def inicio(requests):
    listadoProyecto=Proyecto.objects.all()
    return render(requests,"inicio.html", {'Proyecto':listadoProyecto})


def home(request):
    return render (request, 'home.html')


def desarrolladores(requests):
    listadoDesarrolladores=Desarrollador.objects.all()
    return render(requests,"desarrolladores.html", {'Desarrollador':listadoDesarrolladores})

def nuevoDesarrollador(request):
    return render(request,"nuevoDesarrollador.html")


def nuevoProyecto(request):
    responsable = Desarrollador.objects.all()

    return render(request, "nuevoProyecto.html", {
        'responsable': responsable
    })



def guardarProyecto(request):
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    fecha_inicio = request.POST["fecha_inicio"]
    responsable_id = request.POST["responsable"]

    responsable = Desarrollador.objects.get(id=responsable_id)

    # Crear el proyecto
    Proyecto.objects.create(
        nombre=nombre,
        descripcion=descripcion,
        fecha_inicio=fecha_inicio,
        responsable=responsable
    )

    messages.success(request, "Proyecto guardado exitosamente.")
    return redirect("/inicio")








def guardarDesarrollador(request):
    nombre=request.POST["nombre"]
    apellido=request.POST["apellido"]
    especialidad=request.POST["especialidad"]
    
    nuevoDesarrollador=Desarrollador.objects.create(nombre=nombre,apellido=apellido,especialidad=especialidad)
    messages.success(request,"Desarrollador Guardado Exitosamente")
    return redirect('/desarrolladores')


def editarDesarrollador(request,id):
    desarrolladorEditar=Desarrollador.objects.get(id=id)
    return render(request,"editarDesarrollador.html", {'desarrolladorEditar':desarrolladorEditar})


def actualizandoDesarrollador(request):
    id=request.POST["id"]
    nombre=request.POST["nombre"]
    apellido=request.POST["apellido"]
    especialidad=request.POST["especialidad"]


    
    
    desarrollador=Desarrollador.objects.get(id=id)
    desarrollador.nombre=nombre
    desarrollador.apellido=apellido
    desarrollador.especialidad=especialidad

    
    
    desarrollador.save()
    messages.success(request,"Desarrollador Actualizado Exitosamente")

    return redirect('/desarrolladores')
