from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# Mostra uma mensagem padrão
def hello(request):
    return HttpResponse(f"<h1>Hello World!!!</h1>")


# Soma dois números e retorna o resultado
def sum(request, x, y):
    return HttpResponse(f"<h1>a soma de {x} e {y} é {x+y}</h1>")


# Subtrai um número do outro
def sub(request, x, y):
    return HttpResponse(f"<h1>a soma de {x} e {y} é {x-y}</h1>")


# Multiplica dois números e retorna o resultado
def multi(request, x, y):
    return HttpResponse(f"<h1>a soma de {x} e {y} é {x*y}</h1>")


# Divide dois números e retorna o resultado
def div(request, x, y):
    return HttpResponse(f"<h1>a soma de {x} e {y} é {x/y}</h1>")
