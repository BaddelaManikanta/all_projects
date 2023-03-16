from django.shortcuts import render

# Create your views here.
def operation(request):
    # d={'a':10,'b':204,'c':300}
    d={'name':'MANI','mobile':'9346770752'}
    return render(request,'operation.html',d)