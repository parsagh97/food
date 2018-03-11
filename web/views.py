from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.views.generic import TemplateView
from web.forms import *
# Create your views here.
# def start(request):
#     return render(request ,"startpage.html")

class register(TemplateView):
    template_home = 'startpage.html'

    def get(self, request):
        form = Register()
        return render(request , self.template_home ,{'form':form})

# def register(request):
#     form = Register()
#     return render(request ,"startpage.html" ,{'form':form})