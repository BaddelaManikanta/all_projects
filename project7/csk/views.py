from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dhoni(request):
    return HttpResponse('<h1><marquee>Dhoni is Cool Captain in Cricket!!!!!!!</marquee></h1>')

def rayudu(request):
    return HttpResponse('<h1><marquee>Rayudu is Good Batsman !!!!!!!</marquee></h1>')