from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mani(request):
    return HttpResponse('Hi How Are You')