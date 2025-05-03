from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def projects(request):
    #return HttpResponse('Here are our products')
    return render(request, "projects/projects.html")


def project(request, pk):
    #return HttpResponse('Single projects' + str(pk))
    return render(request, "projects/single-project.html")