from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
    return HttpResponse(f"<h1>Hello World!!!</h1>")


def sum(request, x, y):
    return HttpResponse(f"<h1>a soma de {x} e {y} é {x+y}</h1>")


def multi(request, x, y):
    return HttpResponse(f"<h1>a soma de {x} e {y} é {x*y}</h1>")


def div(request, x, y):
    return HttpResponse(f"<h1>a soma de {x} e {y} é {x/y}</h1>")

