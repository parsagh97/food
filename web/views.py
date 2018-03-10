from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
# Create your views here.
def start(request):
    return render(request ,"startpage.html")
