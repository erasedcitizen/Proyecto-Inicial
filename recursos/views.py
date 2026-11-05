from django.shortcuts import render
from django.http import HttpResponse

def recursos(request):
    return render(request, "recursos/recursos.html")

def derechos_educacionales(request):
    return render(request, "recursos/derechos_educacionales.html")