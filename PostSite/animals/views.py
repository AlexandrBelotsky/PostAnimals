from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, C, C1
from .models import *



#Главная стр
def main(request):
    return render(request, 'animals/main.html')


# Функция регистрации
def registr(request):
    data = {}
    if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
            form.save()
            data['form'] = form
            return redirect('uspex')
    else:
        form = UserCreationForm()
    data['form'] = form
    return render(request, 'animals/registr.html', data)

#Успех регистрации
def uspex(request):
    return render(request, 'animals/uspex_registr.html')

#Аутотенфикация
def user_login(request):
    if request.method == 'POST':
        user_login_form = LoginForm(data=request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return redirect("main")
            else:
                return HttpResponse("Учетная запись или пароль введены неправильно. Пожалуйста, введите заново ~")
        else:
            return HttpResponse("Неверный аккаунт или пароль")
    elif request.method == 'GET':
        user_login_form = LoginForm()
        context = {'form': user_login_form}
        return render(request, 'animals/login.html', context)
    else:
        return HttpResponse("Пожалуйста, используйте GET или POST для запроса данных")


def user_logout(request):
    logout(request)
    return render(request, 'animals/main.html')

#Коммент для свиньи
def pig(request):
    info = Comment_pig.objects.all()
    if request.method == 'POST':
        f = C(request.POST)
        if f.is_valid():
            print(f.cleaned_data)
            f.save()
    else:
        f = C()
    return render(request, 'animals/pig.html', {'f': f, 'info': info})

#Коммент для кенгуру
def kenguru(request):
    info = Comment_kenguru.objects.all()
    if request.method == 'POST':
        f = C1(request.POST)
        if f.is_valid():
            print(f.cleaned_data)
            f.save()
    else:
        f = C1()
    return render(request, 'animals/kenguru.html', {'f': f, 'info': info})