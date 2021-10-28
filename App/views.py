from django.shortcuts import render
from django.http import HttpResponse
from App.models import *


# Create your views here.
def index_views(request):
    diction = {'title':"This is index page"}
    return render(request, 'index.html', context=diction)

def student_views(request):
    diction = {'title':"This is Student page"}
    return render(request, 'student.html', context=diction)