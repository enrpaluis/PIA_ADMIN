from os import link
from winreg import QueryValue
from xml.dom.minidom import Entity
from django.shortcuts import render,redirect, get_list_or_404
from django.http import HttpResponse
from .models import Equipo,Mantenimiento
from .forms import EquipoForm,CustomUserCreationForm, ManteForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import login, authenticate
from qrcode import *
import random
from django.conf import settings
import pickle



def inicio(request):
    return render(request,'paginas/inicio.html')

def reportes(request):
    form=Mantenimiento.objects.all()
    equipos=Equipo.objects.all()
    return render(request,'paginas/reportes.html',{'form':form,'entity':equipos})

def nosotros(request):
    return render(request,'paginas/nosotros.html')

def inventario(request):
    equipos=Equipo.objects.all()
    print(equipos)
    page= request.GET.get('page',1)
    aidi=Equipo.objects.values('id')
    print(aidi)
    values=aidi.values('id')
    print(values)
    y=[]
    for link in values:
        key=('http://127.0.0.1:8000/detalle/'+str(link['id']))
        print(key)
        y.append(key)
    print(y[0])
    
    #except:
     #   raise Http404
   # link = '{0} {1}'.format('Hola',equipo=Equipo.objects.values())
    print(link)
    return render(request,'inventarios/index.html/',{'entity':equipos,'link':link,'key':key,'values':values,'y':y})

def ordenes(request):
    return render(request,'paginas/ordenes.html')

def pendientes(request):
    return render(request,'paginas/pendientes.html')   

def crear_equipo(request):
    formulario=EquipoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Equipo creado correctamente')
        return redirect('inventario')
    return render(request,'inventarios/crear.html',{'formulario':formulario}) 

def editar_equipo(request,id):
    equipo=Equipo.objects.get(id=id)
    formulario=EquipoForm(request.POST or None, request.FILES or None,instance=equipo)
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request,'Equipo editado correctamente')
        return redirect('inventario')
    return render(request,'inventarios/editar.html',{'formulario':formulario,'link':link})


def eliminar(request,id):
    equipo=Equipo.objects.get(id=id)
    equipo.delete()
    messages.success(request,'Equipo eliminado correctamente')
    return redirect('inventario')

def registro(request):
    data = {
        'form':CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request,'Usuario creado correctamente')
            return redirect('inicio')
        else:
            data['form'] = formulario
            messages.error(request,'Error al crear el usuario')
    return render(request,'registration/registro.html',data)

def detalle(request,id):
    form=ManteForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,'Mantenimiento Actualizado')
        return redirect('inventario')
    return render(request,'inventarios/detalle.html',{'form':form,'id':id})


def codigo(request):
   if request.method == "POST":
      Url = request.POST['url']
      img = make(Url)
      img_name = f'qrimg{random.randint(1, 1000)}.png'
      img.save(settings.MEDIA_ROOT/img_name)
      return render(request,"index.html", {'img':img_name,'id':id})
   return render(request,"index.html")

def codigo_qr(request,id):
   if request.method=="POST":
      Url=request.POST['url']

def scanner(request):
   return render(request,"scanner.html")
