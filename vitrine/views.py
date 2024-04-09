from django.shortcuts import render, redirect
from .forms import BmrForm, PlanForm
import requests
from django.http import JsonResponse
import json

def accueil_site(request):
    reqUrl = "http://localhost:3333/getkalperday"

    if request.method == 'POST':
        form = BmrForm(request.POST)
        
        if form.is_valid():
            sex = form.cleaned_data["sex"]
            age = form.cleaned_data["age"]
            weight = form.cleaned_data["weight"]
            size = form.cleaned_data["size"]
            
            
            headers = {
                'Content-Type': 'application/json'
            }
            
            payload = json.dumps({
                "sex": sex,
                "age": age,
                "weight": weight,
                "size": size,
            })

            response = requests.request("POST",reqUrl, headers=headers, data=payload)
            if response.status_code == 200:
                bmr_data = response.json()
                api_bmr = bmr_data.get('YourBMR', None)
                if api_bmr:
                    request.session['api_bmr'] = api_bmr
                    return redirect('bmr-url')
                else:
                    return JsonResponse({"message": "Erreur: Aucun BMR trouvé dans la réponse de l'API"})
            else :
                return JsonResponse({"message": f"Erreur: {response.status_code} - {response.text}"}, status=response.status_code)
    else:
        return render(request, "accueil.html")

def bmr_site(request):
    api_bmr = request.session.get('api_bmr')
    print(api_bmr)
    reqUrl = "http://localhost:3333/generate-meals"

    if request.method == 'POST':
        form = PlanForm(request.POST)
        
        if form.is_valid():
            typePlan = form.cleaned_data["typePlan"]
            userMail = form.cleaned_data["userMail"]
            
            
            headers = {
                'Content-Type': 'application/json'
            }
            
            payload = json.dumps({
                "BMR": api_bmr,
                "typePlan": typePlan,
                "userMail": userMail,
            })

            response = requests.request("POST", reqUrl, headers=headers, data=payload)
            print(response)
            return redirect('merci-url')
            
    else:
        context = {'api_bmr': api_bmr}
    return render(request, "bmr.html", context=context)

def merci_site(request):
    return render(request, "merci.html")