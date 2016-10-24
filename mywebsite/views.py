from django.shortcuts import render
from django.http import HttpResponse

def webdev(request):
    return render(request, 'webdev.html', {})
def tuition(request):
    return render(request, 'tuition.html', {})
   
