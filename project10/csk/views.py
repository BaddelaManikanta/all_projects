from django.shortcuts import render

# Create your views here.
def dhoni(request):
    D={'name':'DHONI','age':50,'award':'MR.Cool'}
    return render(request,'dhoni.html',context=D)