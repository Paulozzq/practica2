from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario 

def login_mostrar(request):
    return render(request, 'index.html') 

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            usuario = Usuario.objects.get(username=username)
            if usuario.password == password:
                return render(request, 'productos.html')
            else:
                return render(request, 'index.html', {'error_message': "Error: Contraseña incorrecta."})
        except Usuario.DoesNotExist:
            return render(request, 'index.html', {'error_message': "Error: El usuario no existe."})

    return render(request, 'index.html') 

def registro(request):
    error_message = ""  
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if Usuario.objects.filter(username=username).exists():
            error_message = "El nombre de usuario ya existe. Por favor elige otro."
        else:
            usuario = Usuario(username=username, password=password)
            usuario.save()
            return HttpResponse('Usuario guardado correctamente.')

    return render(request, 'index.html', {'error_message': error_message})
