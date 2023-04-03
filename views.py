from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def faculty(request):
    return render(request, 'faculty.html')


def parent(request):
    return render(request, 'parent.html')


def student(request):
    return render(request, 'student.html')


def base(request):
    return render(request, 'base.html')


def home(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/home/')
    return render(request, 'home.html')
