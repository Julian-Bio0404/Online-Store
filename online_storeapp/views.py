"""Views ProyectoWebApp"""

from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "online_storeapp/home.html")