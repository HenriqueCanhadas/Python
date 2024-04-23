from django.shortcuts import render
from .models import Usuario

# Create your views here.

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    usuarios = {
        'usuarios':Usuario.objects.all()
    }

    return render(request, 'usuarios/usuarios.html', usuarios)
