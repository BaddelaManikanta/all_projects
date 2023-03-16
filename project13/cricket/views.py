from django.shortcuts import render

# Create your views here.
def dhoni(request):
    return render(request,'dhoni.html')

def sachin(request):
    return render(request,'sachin.html')