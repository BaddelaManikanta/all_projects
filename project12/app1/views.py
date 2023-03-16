from django.shortcuts import render

# Create your views here.
def first(request):
    d={'fn': 'MANIKANTA'}
    return render(request,'first.html',d)

def last(request):
    d1={'ln':'BADDELA'}
    return render(request,'last.html',d1)