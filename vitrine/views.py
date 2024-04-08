from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from .forms import InfoForm
import requests
from django.http import JsonResponse
import json

# Create your views here.

def accueil_site(request):
    reqUrl = "http://192.168.0.10/getkalperday"

    if request.method == 'POST':
        form = InfoForm(request.POST)
        
        if form.is_valid():
            sex = form.cleaned_data["sex"]
            age = form.cleaned_data["age"]
            size = form.cleaned_data["size"]
            weight = form.cleaned_data["weight"]
            
            
            headersList = {
                'Content-Type': 'application/json'
            }
            
            payload = json.dumps({
                "sex": sex,
                "age": age,
                "size": size,
                "weight": weight,
            })

            response = requests.post(reqUrl, headers=headersList, data=payload)
            print(response)
            return render(request, "accueil.html")
    else:
        form = InfoForm()
    return render(request, "accueil.html", {'form': form})