from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .backends import RegistroBackend
from .forms import LoginForm, RegistroForm
from .models import Registro

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            usuario = authenticate(request, email=email, password=password)

            if usuario is not None:
                login(request, usuario) 
                return redirect('inicio')
            else:
                form.add_error(None, 'Usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('inicio')
    else:
        form = RegistroForm()
    
    return render(request, 'accounts/registro.html', {'form': form})

@login_required(login_url='login')
def inicio_view(request):
    next_url = request.GET.get('next')
    if next_url:
        return redirect(next_url)
    else:
        return render(request, 'accounts/inicio.html')