from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

# Create your views here.

def accueil_site(request):
    return render(request, "accueil.html")