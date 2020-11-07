from django.http import HttpResponse
from django.shortcuts import render

# method view
def index(request):
    return render(request,'index.html')

def index2(request):
    return HttpResponse("<h1> Hello World </h1>")

def about(request):
    return HttpResponse("<h1> ini about </h1>")