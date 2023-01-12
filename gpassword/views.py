from django.shortcuts import render
from random import choice


# Create your views here.

def home(request):
    return render(request, 'gpassword/home.html')


def about(reguest):
    return render(reguest, 'gpassword/about.html')


def generator(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('AASFAGFFB')

    if request.GET.get('numbers'):
        characters.extend('12345436w34')

    length = int(request.GET.get('length',12))
    password = []
    for i in range(length):
        password.append(choice(characters))

    return render(request, 'gpassword/password.html', {'password': password})
