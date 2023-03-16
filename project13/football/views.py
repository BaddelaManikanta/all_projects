from django.shortcuts import render

# Create your views here.
def ronaldo(request):
    return render(request,'ronaldo.html')

def messi(request):
    return render(request,'messi.html')