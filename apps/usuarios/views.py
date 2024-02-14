from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from apps.usuarios.forms import LoginForms, CadastroForms


def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form["nome_login"].value()
            senha = form["senha_login"].value()
                
            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                return redirect('index')
            else:
                messages.error(request, "usuário ou senha inválido")
                return redirect('login')

    return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            if form["senha_cadastro"].value() != form["senha_confirma"].value():
                messages.error(request, "senhas não são iguais")
                return redirect('cadastro')

            nome = form["nome_cadastro"].value()
            email = form["email"].value()
            senha = form["senha_cadastro"].value()

        if  User.objects.filter(username=nome).exists():
            messages.error(request, "Usuário já existente")
            return redirect('cadastro')
        
        usuario =  User.objects.create_user(
            username=nome,
            email=email,
            password=senha
        )
        usuario.save()
        messages.success(request, "Cadastro efetuado com sucesso")
        return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form": form})

def logout(request):
    messages.success(request, "Logout efetuado com sucesso")
    auth.logout(request)
    return redirect('login')

