from django.shortcuts import render
from  django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return HttpResponse("<h1>WHAT YOU WANT TO KNOW ABOUT ME?!?!?!</h1>")