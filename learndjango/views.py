# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("This is HomPage")
    return render(request, 'home.html')

def aboutpage(reuqest):
    # return HttpResponse("This is AboutPage")
    return render(reuqest, 'about.html')

