from django.shortcuts import render

# Create your views here.
def hardik(request):
    d={'name':'HARDIK PANDYA','age':35,'award':'BEST BATSMAN'}
    return render(request,'hardik.html',context=d)
