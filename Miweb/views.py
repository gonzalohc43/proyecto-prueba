
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from Miweb.forms import Registro


def index(request):
   return render(request,'index.html',{
       'title': 'Personas',
       'personas':[
        {'nombre':'Felipe','edad':22,'sexo':'Masculino'},
        {'nombre':'Gonzalo','edad':35,'sexo':'Masculino'},
        {'nombre':'Maria','edad':5,'sexo':'Femenino'},
        {'nombre':'Hortencia','edad':32,'sexo':'Femenino'}
        
       ]
    
    } )


def login_view(request): 
   username = None
   password = None
   
   if request.method == "POST":
      username = request.POST.get('username')
      password = request.POST.get('password')


   usuario = authenticate(username=username,password=password)

   if usuario:
      login(request,usuario)
      messages.success(request,f'Bienvenido,{usuario.username}')
      return redirect('index') 
   else:
      messages.error(request,'Datos invalidos')     

   return render(request, 'usuarios/login.html', {})  
   

def salir(request):
      logout(request)
      messages.success(request , 'Sesion cerrada con exito')
      return redirect('login')


def registro(request):
   form = Registro(request.POST or None)
   
   if request.method == 'POST' and form.is_valid():
      username = form.cleaned_data.get('username')
      email = form.cleaned_data.get('email')
      password = form.cleaned_data.get('password')

      usuario = User.objects.create_user(username,email,password)

   if usuario:
      login(request,usuario)
      messages.success(request,'Enhorabuena registro existoso!')
      return redirect('index')   
   
   
   return render(request, 'usuarios/registro.html', {
      
      'form': form,
})      
