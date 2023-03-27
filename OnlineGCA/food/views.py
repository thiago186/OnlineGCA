from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def TestHomeView(request):
    return HttpResponse('Hello World')

def TestItem(request):
    return HttpResponse('This is a testing view for an item.')