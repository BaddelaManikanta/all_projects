from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rohit(request):
    return HttpResponse('<h1><marquee><a href="rohit">HI MI FANS .. Rohit is Hit Batsman in Cricket!!!!!!!</marquee></h1>')
