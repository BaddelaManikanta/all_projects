from django.shortcuts import render
# Create your views here.

def mi(request):
    d={'name':'mani','mobile':9346770752}
    return render(request,'mi.html',context=d)